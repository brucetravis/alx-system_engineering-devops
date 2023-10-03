#!/usr/bin/env ruby

def beginning_and_end(str)
  pattern = /^h.n$/
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

beginning_and_end(ARGV[0])
