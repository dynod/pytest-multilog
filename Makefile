# Makefile for pytest-multilog project

# Setup roots
WORKSPACE_ROOT := $(CURDIR)/../..
PROJECT_ROOT := $(CURDIR)

# Python package name
PYTHON_PACKAGE := pytest-multilog

# Main makefile suite - defs
include $(WORKSPACE_ROOT)/.workspace/main.mk

# Default target is to build Python artifact
default: build

# Main makefile suite - rules
include $(WORKSPACE_ROOT)/.workspace/rules.mk
