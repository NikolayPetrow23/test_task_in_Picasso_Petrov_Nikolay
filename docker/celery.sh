#!/bin/bash

celery -A file_project.file_project worker --loglevel=info
