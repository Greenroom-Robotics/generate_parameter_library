#!/usr/bin/env python3
"""Allow running validate_schema as a module: python -m validate_schema"""
import sys
from validate_schema import main

if __name__ == '__main__':
    sys.exit(main())
