#!/bin/bash
esphome compile $1
esphome compile $1
while ! esphome upload $1; do :; done
esphome logs $1