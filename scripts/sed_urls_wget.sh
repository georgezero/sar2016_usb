#!/bin/bash

sed -ne 's/.*\(https[^")]*.woff2\).*/\1/p' < fonts.css | xargs wget
