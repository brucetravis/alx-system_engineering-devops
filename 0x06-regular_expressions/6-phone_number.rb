#!/usr/bin/env ruby

def phone_number(str)
  pattern = /^\d{10}$/
  match = str.match(pattern)

  if match
    puts "#{match[0]}$"
  else
    puts "$"
  end
end

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

phone_number(ARGV[0])
