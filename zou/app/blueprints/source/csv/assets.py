from zou.app.blueprints.source.csv.base import BaseCsvProjectImportResource

from zou.app.services import assets_service, projects_service, shots_service
from zou.app.models.entity import Entity

from sqlalchemy.exc import IntegrityError


class AssetsCsvImportResource(BaseCsvProjectImportResource):
    def prepare_import(self, project_id):
        self.episodes = {}
        self.entity_types = {}
        self.descriptor_fields = self.get_descriptor_field_map(
            project_id, "Asset"
        )
        project = projects_service.get_project(project_id)
        self.is_tv_show = projects_service.is_tv_show(project)
        if self.is_tv_show:
            episodes = shots_service.get_episodes_for_project(project_id)
            self.episodes = {
                episode["name"]: episode["id"]
                for episode in episodes
            }

    def import_row(self, row, project_id):
        asset_name = row["Name"]
        entity_type_name = row["Type"]
        description = row["Description"]
        episode_name = row.get("Episode", None)
        episode_id = None
        if episode_name is not None:
            episode_id = self.episodes.get(episode_name, None)

        self.add_to_cache_if_absent(
            self.entity_types,
            assets_service.get_or_create_asset_type,
            entity_type_name,
        )
        entity_type_id = self.get_id_from_cache(
            self.entity_types, entity_type_name
        )

        data = {}
        for name, field_name in self.descriptor_fields.items():
            if name in row:
                data[field_name] = row[name]

        try:
            entity = Entity.get_by(
                name=asset_name,
                project_id=project_id,
                entity_type_id=entity_type_id,
                source_id=episode_id
            )
            if entity is None:
                entity = Entity.create(
                    name=asset_name,
                    description=description,
                    project_id=project_id,
                    entity_type_id=entity_type_id,
                    source_id=episode_id,
                    data=data,
                )
            else:
                entity.update({"description": description, "data": data})
        except IntegrityError:
            pass

        return entity.serialize()
