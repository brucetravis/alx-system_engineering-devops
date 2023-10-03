#!/usr/bin/env ruby

def process_log_line(line)
  sender = line.match(/\[from:([^[\]]+)\]/)&.captures&.first || "Unknown"
  receiver = line.match(/\[to:([^[\]]+)\]/)&.captures&.first || "Unknown"
  flags = line.match(/\[flags:([^[\]]+)\]/)&.captures&.first || "Unknown"

  "#{sender},#{receiver},#{flags}"
end

def textme_statistics(log_file_path)
  File.open(log_file_path, "r") do |file|
    file.each_line do |line|
      if line.include?("mdr: Sent SMS") || line.include?("mdr: Receive SMS")
        puts process_log_line(line)
      end
    end
  end
end

if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} <log_file_path>"
  exit 1
end

textme_statistics(ARGV[0])
