#!/usr/bin/env ruby

def match_school(str)
  pattern = /School/
  match = str.match(pattern)

  if match
    puts "Match: #{match[0]}$"
  else
    puts "$"
  end
end

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

match_school(ARGV[0])
