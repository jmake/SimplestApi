git clone https://github.com/YunzheZJU/youtube-po-token-generator.git  

npm install jsdom
#node youtube-po-token-generator/examples/one-shot.js

output=$(node youtube-po-token-generator/examples/one-shot.js)

# Print the raw output for debugging
echo "Raw Output:"
echo "$output"

# Extract visitorData and poToken manually
visitorData=$(echo "$output" | sed -n "s/.*visitorData: '\([^']*\)'.*/\1/p")
poToken=$(echo "$output" | sed -n "s/.*poToken: '\([^']*\)'.*/\1/p")

echo -e "${visitorData}\n${poToken}"

# Run the Python script with the extracted values
echo -e "${visitorData}\n${poToken}" | python youtube_tools.py

