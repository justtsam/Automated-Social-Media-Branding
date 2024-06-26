import facebook

# Create a Facebook Graph API object
access_token = 'EAAHnZC1I0N8EBAOevNcECIhIi3FYvqwINfZBfmjwHwbwoZCbCzdCcEU7cYS8YfSnFjpsZBc2G8k9pcTMj5l8OP7tVGj7t78IINL8mlIwZCzcqBGpTFzCnTTZAkdvkacmd06No7Jd6KXvYLrRXh6rFPIsKDsAFjkyVDSWHeXeAfqwY1RQu23wmiumcoQw9ZAzyjpemH5xlfOuyzqRxNNJ8kPPemH4QZBJ4FUZD'
graph = facebook.GraphAPI('EAAHnZC1I0N8EBAOevNcECIhIi3FYvqwINfZBfmjwHwbwoZCbCzdCcEU7cYS8YfSnFjpsZBc2G8k9pcTMj5l8OP7tVGj7t78IINL8mlIwZCzcqBGpTFzCnTTZAkdvkacmd06No7Jd6KXvYLrRXh6rFPIsKDsAFjkyVDSWHeXeAfqwY1RQu23wmiumcoQw9ZAzyjpemH5xlfOuyzqRxNNJ8kPPemH4QZBJ4FUZD')

# Upload a photo to a Facebook album

photo_id= graph.put_photo(image=open(r'C:/Users/sam/Pictures/Screenshots/Screenshot (64).png', 'rb'), album_path='100090973306447 /photos')

# Add a caption to the photo
graph.put_object(parent_object=photo_id, connection_name='captions', message='This is my photo caption!')

# Post a message on Facebook
graph.put_object(parent_object='me', connection_name='feed', message='This is my message!')