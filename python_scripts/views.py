from rest_framework.views import APIView
from python_project.settings import JOKES_URL
import requests
from .models import Jokes
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class JokesData(APIView):
    """
    call jokes api and append it to database and display in front end
    """
    @staticmethod
    def post(request):
        number_of_jokes = request.data.get('number_of_jokes', 1)

        if not isinstance(number_of_jokes, int) or number_of_jokes < 1:
            return Response({"error": "number_of_jokes must be a positive integer."}, 
                            status=status.HTTP_400_BAD_REQUEST)

        url = JOKES_URL
        jokes_to_store = []
        data_stored = []
        # Fetch 100 jokes
        for _ in range(number_of_jokes):
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    data_stored.append(data)
                    # Process and store the joke based on its type
                    joke_data = {
                        'category': data['category'],
                        'joke_type': data['type'],
                        'nsfw': data['flags']['nsfw'],
                        'political': data['flags']['political'],
                        'sexist': data['flags']['sexist'],
                        'safe': data['safe'],
                        'lang': data['lang'],
                        'joke': "",
                        'setup': "",
                        'delivery': ""
                    }

                    if data['type'] == 'single':
                        joke_data['joke'] = data['joke']
                    else:  # type is 'twopart'
                        joke_data['setup'] = data['setup']
                        joke_data['delivery'] = data['delivery']

                    # Create a new Joke instance
                    jokes_to_store.append(Jokes(**joke_data))

                except ValueError:
                    return Response({"error": "Failed to decode JSON"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({"error": f"Failed to fetch from API: {response.status_code}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Store jokes in bulk to the database
        if jokes_to_store:
            Jokes.objects.bulk_create(jokes_to_store)
            return Response({"message": "Jokes fetched and stored successfully",
                             "jokes": data_stored}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "No jokes to store"}, status=status.HTTP_204_NO_CONTENT)