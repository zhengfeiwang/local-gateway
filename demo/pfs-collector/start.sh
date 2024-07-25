#!/bin/bash

pf service start

# keep the container running
tail -f /dev/null
