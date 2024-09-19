def hex_to_wav(input_file, output_file):
    with open(input_file, 'r') as hex_file:
        # Read the entire file as a string
        hex_string = hex_file.read()
        
        # Split the string into a list of hex values
        hex_values = hex_string.split()
        
        # Convert the hex values to byte data
        byte_data = bytes(int(hv, 16) for hv in hex_values)
        
        # Write the byte data to the output file
        with open(output_file, 'wb') as wav_file:
            wav_file.write(byte_data)

# Usage example
input_file = 'output.data'
output_file = 'restored.scndef'
hex_to_wav(input_file, output_file)
