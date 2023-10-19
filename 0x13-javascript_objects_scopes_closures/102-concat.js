#!/usr/bin/node
import { readFileSync, writeFileSync } from 'fs';

const firstArg = readFileSync(process.argv[2]).toString();
const secondArg = readFileSync(process.argv[3]).toString();
writeFileSync(process.argv[4], firstArg + secondArg);
