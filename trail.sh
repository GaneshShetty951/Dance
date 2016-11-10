echo "Enter the pattern :"
read pat
echo "Enter the filename :"
read filename
grep "$pat" "$filename" || echo "Pattern found"
