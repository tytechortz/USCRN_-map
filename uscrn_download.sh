#!/bin/bash

while read FILE; do
   LINK="https://www1.ncdc.noaa.gov/pub/data/uscrn/products/monthly01/${FILE}"
   wget $LINK
done < <(cat index.html | grep txt | awk '{print $5}' | cut -d '"' -f2)

cat *.txt > all_uscrn__data.txt