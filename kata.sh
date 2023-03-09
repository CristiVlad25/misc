#!/bin/bash

# Parse arguments
while getopts ":d:c:p:ef:u:cs:" opt; do
  case ${opt} in
    d )
      depth=$OPTARG
      ;;
    c )
      concurrency=$OPTARG
      ;;
    p )
      threads=$OPTARG
      ;;
    ef )
      extensions=$OPTARG
      ;;
    u )
      tld=$OPTARG
      ;;
    cs )
      restrict=$OPTARG
      ;;
    \? )
      echo "Invalid option: -$OPTARG" 1>&2
      exit 1
      ;;
    : )
      echo "Option -$OPTARG requires an argument." 1>&2
      exit 1
      ;;
  esac
done

# Check if top level domain is provided
if [ -z "${tld}" ]
then
  if [ -z "$1" ]
  then
    echo "Top level domain argument is missing. Usage: $0 [-u <tld>] <tld>" >&2
    exit 1
  else
    tld=$1
  fi
fi

# Prepend the TLD with the https:// prefix
tld="https://${tld}"

# Set default value for the restrict argument if not provided
if [ -z "${restrict}" ]
then
  restrict="^.*\.?$(echo ${tld} | sed 's|https\?://||' | sed 's|/.*||').*$"
fi

# Run Katana command
katana -d ${depth:-5} -c ${concurrency:-50} -p ${threads:-20} -ef ${extensions:-"ttf,woff,svg,jpeg,jpg,png,ico,gif,css"} -u ${tld} -cs "${restrict}"
