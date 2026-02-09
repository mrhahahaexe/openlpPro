# -*- coding: utf-8 -*-

##########################################################################
# OpenLP - Open Source Lyrics Projection                                 #
# ---------------------------------------------------------------------- #
# Copyright (c) 2008 OpenLP Developers                                   #
# ---------------------------------------------------------------------- #
# This program is free software: you can redistribute it and/or modify   #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation, either version 3 of the License, or      #
# (at your option) any later version.                                    #
#                                                                        #
# This program is distributed in the hope that it will be useful,        #
# but WITHOUT ANY WARRANTY; without even the implied warranty of         #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
# GNU General Public License for more details.                           #
#                                                                        #
# You should have received a copy of the GNU General Public License      #
# along with this program.  If not, see <https://www.gnu.org/licenses/>. #
##########################################################################
"""
The :mod:`~openlp.core.lib.recognition` module provides song recognition capabilities.
"""
import logging
import json
import requests
from PySide6 import QtCore

from openlp.core.common.registry import Registry

log = logging.getLogger(__name__)

class RecognitionService(QtCore.QObject):
    """
    Service to recognize songs from audio data using AI APIs.
    """
    song_recognized = QtCore.Signal(str, str)  # title, artist
    verse_recognized = QtCore.Signal(int)      # slide index

    def __init__(self, parent=None):
        super().__init__(parent)
        self.api_key = "" # To be loaded from settings

    def process_audio(self, audio_bytes):
        """
        Process the captured audio bytes to recognize the song.
        """
        log.debug("Processing audio for recognition...")
        
        # MOCK LOGIC for demonstration
        # In a real implementation, this would call ACRCloud or OpenAI Whisper
        
        # Simulate a delay
        QtCore.QTimer.singleShot(1000, lambda: self._on_recognition_success("Amazing Grace", "John Newton"))

    def _on_recognition_success(self, title, artist):
        log.info(f"AI Recognized Song: {title} by {artist}")
        self.song_recognized.emit(title, artist)
        
        # After recognizing the song, we would start another process 
        # to track the live position (lyric sync)
        # For now, let's just emit the signal
        
    def track_lyrics(self, audio_bytes, current_item):
        """
        Track live lyrics and identify the current verse.
        """
        log.debug("Tracking lyrics for live sync...")
        # In a real implementation, this would use Whisper to get text
        # transcribed_text = self.whisper.transcribe(audio_bytes)
        
        # MOCK TRANSCRIBED TEXT for demonstration
        # Let's say we are singing the first few words of a verse
        verses = current_item.get_frames()
        # Find the best match
        # For mock, we'll just periodically jump to the next slide
        current_row = Registry().get('live_controller').selected_row
        next_row = (current_row + 1) % len(verses)
        
        log.info(f"AI Sync: Jumping to slide {next_row}")
        self.verse_recognized.emit(next_row)

    def match_lyrics(self, recognized_text, verses):
        """
        Find the index of the verse that best matches the recognized text.
        """
        best_match_index = -1
        highest_score = 0
        
        recognized_words = set(recognized_text.lower().split())
        
        for i, verse in enumerate(verses):
            verse_words = set(verse['text'].lower().split())
            overlap = len(recognized_words.intersection(verse_words))
            if overlap > highest_score:
                highest_score = overlap
                best_match_index = i
        
        return best_match_index
