#!/usr/bin/awk -f

{
    # Match the pattern ZZ(something)   // comments
    if ($0 ~ /ZZ\([^)]*\)\s*\/\/.*/) {
        # Extract "something" and "comments"
        match($0, /ZZ\(([^)]*)\)\s*\/\/\s*(.*)/, arr);
        something = arr[1];
        comments = arr[2];
        # Replace commas in "something" with spaces
        gsub(/,/, " ", something);
        # Print in the .md format used for mkdocs 
        printf "\n\n```<%s>```\n\n%s\n", something, comments;
    } 
}
