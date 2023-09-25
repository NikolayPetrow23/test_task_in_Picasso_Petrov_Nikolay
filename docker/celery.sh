#!/bin/bash

cd file_project

celery --app=file_project.celery worker -l INFO
