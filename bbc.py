{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "bbc.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOqhVSMm4aIO+RFGdGQER3b",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/eboueleamana/WebScraping/blob/master/bbc.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sGJA2gDPS80L",
        "outputId": "2cf6afaf-dbf6-4497-b15e-e0d8ea8e47ce"
      },
      "source": [
        "pip install beautifulsoup4"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.7/dist-packages (4.6.3)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fhF749KWTu_x",
        "outputId": "9b6924b8-eead-49a4-8fa0-6efdbce100b0"
      },
      "source": [
        "pip install requests"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: requests in /usr/local/lib/python3.7/dist-packages (2.23.0)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests) (2.10)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests) (3.0.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests) (2021.5.30)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests) (1.24.3)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qu2SjdfIT2Cx"
      },
      "source": [
        "import requests\n",
        "from bs4 import BeautifulSoup\n",
        "import pandas as pd\n"
      ],
      "execution_count": 10,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fe876qd0Um8M"
      },
      "source": [
        "url=\"http://feeds.bbci.co.uk/news/rss.xml\""
      ],
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AnDN3Hv1WgjZ"
      },
      "source": [
        "#import le code de la page\n",
        "reponse=requests.get(url)\n",
        "soup = BeautifulSoup(reponse.text,\"html.parser\")\n",
        "soup"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "U1gevN39aaje"
      },
      "source": [
        "items = soup.findAll('item')"
      ],
      "execution_count": 15,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gfaCLR6taxfR"
      },
      "source": [
        "items"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "_8Pcs-qGcg2I",
        "outputId": "8f22d0dd-5fdd-4f3b-d255-356cc51d83bc"
      },
      "source": [
        "item=items[0]\n",
        "item.description.text"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'Military drivers will be trained up as a precaution, after days of long queues and pump closures.'"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "sfh0mggecvM3"
      },
      "source": [
        "news_items=[]"
      ],
      "execution_count": 19,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_8qPkoipdGL7"
      },
      "source": [
        "for i in items:\n",
        "  news_i={}\n",
        "  news_i['title']= i.title.text\n",
        "  news_i['description']= i.description.text\n",
        "  news_i['pubdate']= i.pubdate.text\n",
        "  news_items.append(news_i)"
      ],
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "YZ7RDLFefyM_"
      },
      "source": [
        "news_items"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "4ImysNjBlBlR"
      },
      "source": [
        "#Convertir la liste en base de donnés\n",
        "df=pd.DataFrame(news_items,columns=['title','description','pubdate'])\n",
        "df.head"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IsI4q7PalyjC"
      },
      "source": [
        "#Générer le fichier CVS\n",
        "\n",
        "df.to_csv('web_scraping.csv', index=False, encoding='utf-8')"
      ],
      "execution_count": 24,
      "outputs": []
    }
  ]
}