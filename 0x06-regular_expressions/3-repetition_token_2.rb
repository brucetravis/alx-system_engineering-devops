#!/usr/bin/env ruby

def repetition_token(str)
  pattern = /h.{0,1}tn/
  match = str.match(pattern)

  if match
    puts match[0]
  else
    puts "No match"
  end
end

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

repetition_token(ARGV[0])
