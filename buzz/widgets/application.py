import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication

from buzz.__version__ import VERSION
from buzz.db.dao.transcription_dao import TranscriptionDAO
from buzz.db.dao.transcription_segment_dao import TranscriptionSegmentDAO
from buzz.db.db import setup_app_db
from buzz.db.service.transcription_service import TranscriptionService
from buzz.settings.settings import APP_NAME, Settings

from buzz.transcriber.transcriber import FileTranscriptionTask
from buzz.widgets.main_window import MainWindow


class Application(QApplication):
    window: MainWindow

    def __init__(self, argv: list) -> None:
        super().__init__(argv)

        self.setApplicationName(APP_NAME)
        self.setApplicationVersion(VERSION)

        self.settings = Settings()
        font_size = self.settings.value(
            key=Settings.Key.FONT_SIZE, default_value=self.font().pointSize()
        )

        if sys.platform == "darwin":
            self.setFont(QFont("SF Pro", font_size))
        else:
            self.setFont(QFont(self.font().family(), font_size))


        db = setup_app_db()
        transcription_service = TranscriptionService(
            TranscriptionDAO(db), TranscriptionSegmentDAO(db)
        )

        self.window = MainWindow(transcription_service)
        self.window.show()

    def add_task(self, task: FileTranscriptionTask):
        self.window.add_task(task)
