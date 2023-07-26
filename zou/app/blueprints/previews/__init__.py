from flask import Blueprint
from zou.app.utils.api import configure_api_from_blueprint

from zou.app.blueprints.previews.resources import (
    CreatePreviewFilePictureResource,
    PreviewFileLowMovieResource,
    PreviewFileMovieResource,
    PreviewFileMovieDownloadResource,
    PreviewFileThumbnailResource,
    PreviewFileResource,
    PreviewFileDownloadResource,
    PreviewFileThumbnailSquareResource,
    PreviewFilePreviewResource,
    PreviewFileOriginalResource,
    CreateOrganisationThumbnailResource,
    OrganisationThumbnailResource,
    CreateProjectThumbnailResource,
    ProjectThumbnailResource,
    CreatePersonThumbnailResource,
    PersonThumbnailResource,
    RunningPreviewFiles,
    LegacySetMainPreviewResource,
    SetMainPreviewResource,
    UpdateAnnotationsResource,
    UpdatePreviewPositionResource,
    ExtractFrameFromPreview,
    ExtractTileFromPreview,
)

routes = [
    ("/data/playlists/preview-files/running", RunningPreviewFiles),
    (
        "/pictures/preview-files/<instance_id>",
        CreatePreviewFilePictureResource,
    ),
    (
        "/movies/originals/preview-files/<instance_id>.mp4",
        PreviewFileMovieResource,
    ),
    (
        "/movies/originals/preview-files/<instance_id>/download",
        PreviewFileMovieDownloadResource,
    ),
    (
        "/movies/low/preview-files/<instance_id>.mp4",
        PreviewFileLowMovieResource,
    ),
    (
        "/pictures/thumbnails/preview-files/<instance_id>.png",
        PreviewFileThumbnailResource,
    ),
    (
        "/pictures/thumbnails-square/preview-files/<instance_id>.png",
        PreviewFileThumbnailSquareResource,
    ),
    (
        "/pictures/originals/preview-files/<instance_id>.png",
        PreviewFileOriginalResource,
    ),
    (
        "/pictures/originals/preview-files/<instance_id>.<extension>",
        PreviewFileResource,
    ),
    (
        "/pictures/originals/preview-files/<instance_id>/download",
        PreviewFileDownloadResource,
    ),
    (
        "/pictures/previews/preview-files/<instance_id>.png",
        PreviewFilePreviewResource,
    ),
    (
        "/pictures/thumbnails/organisations/<instance_id>",
        CreateOrganisationThumbnailResource,
    ),
    (
        "/pictures/thumbnails/organisations/<instance_id>.png",
        OrganisationThumbnailResource,
    ),
    (
        "/pictures/thumbnails/persons/<instance_id>",
        CreatePersonThumbnailResource,
    ),
    (
        "/pictures/thumbnails/persons/<instance_id>.png",
        PersonThumbnailResource,
    ),
    (
        "/pictures/thumbnails/projects/<instance_id>",
        CreateProjectThumbnailResource,
    ),
    (
        "/pictures/thumbnails/projects/<instance_id>.png",
        ProjectThumbnailResource,
    ),
    (
        "/actions/entities/<entity_id>/set-main-preview/<preview_file_id>",
        LegacySetMainPreviewResource,
    ),
    (
        "/actions/preview-files/<preview_file_id>/set-main-preview",
        SetMainPreviewResource,
    ),
    (
        "/data/preview-files/<preview_file_id>/extract-frame",
        ExtractFrameFromPreview,
    ),
    (
        "/actions/preview-files/<preview_file_id>/update-position",
        UpdatePreviewPositionResource,
    ),
    (
        "/actions/preview-files/<preview_file_id>/update-annotations",
        UpdateAnnotationsResource,
    ),
    (
        "/data/preview-files/<preview_file_id>/extract-frame",
        ExtractTileFromPreview,
    ),
]
blueprint = Blueprint("thumbnails", "thumbnails")
api = configure_api_from_blueprint(blueprint, routes)
