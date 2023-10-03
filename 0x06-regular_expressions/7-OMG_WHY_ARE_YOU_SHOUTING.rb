#!/usr/bin/env ruby

def shouting(text)
  pattern = /[A-Z]/
  matches = text.scan(pattern)

  if matches.any?
    puts matches.join('')
  else
    puts "$"
  end
end

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

shouting(ARGV[0])
