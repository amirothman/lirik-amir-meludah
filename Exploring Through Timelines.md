# Exploring Through Timelines
# Looking At How Public People and Ideas Change Through Time

The news is one of our main sources of information. We feel the presence of distant others through news stories. This writing is intended to demonstrate an example of combining computer science with journalism. Computing digital humanities. We explain in detail how.

"RSS (Rich Site Summary; originally RDF Site Summary; often called Really Simple Syndication) uses a family of standard web feed formats to publish frequently updated information: blog entries, news headlines, audio, video. An RSS document (called "feed", "web feed", or "channel") includes full or summarized text, and metadata, like publishing date and author's name."

https://en.wikipedia.org/wiki/RSS

"Twitter is an online news and social networking service where users post and interact with messages, "tweets," restricted to 140 characters. Registered users can post tweets, but those who are unregistered can only read them. Users access Twitter through its website interface, SMS or a mobile device app. Twitter Inc. is based in San Francisco and has more than 25 offices around the world."

        https://en.wikipedia.org/wiki/Twitter

"A timeline is a way of displaying a list of events in chronological order, sometimes described as a project artifact. It is typically a graphic design showing a long bar labeled with dates alongside itself and usually events"

        https://en.wikipedia.org/wiki/Timeline

"HyperText Markup Language (HTML) is the standard markup language for creating web pages and web applications. With Cascading Style Sheets (CSS), and JavaScript, it forms a triad of cornerstone technologies for the World Wide Web. Web browsers receive HTML documents from a web server or from local storage and render them into multimedia web pages. HTML describes the structure of a web page semantically and originally included cues for the appearance of the document."

        https://en.wikipedia.org/wiki/HTML

"Online publications or network publications are electronic publications, which are not offered on a physical medium, but via the Internet”

        Google translated to English with manual edit,
        https://de.wikipedia.org/wiki/Online-Publikation


"In computing, a news aggregator, also termed a feed aggregator, feed reader, news reader, RSS reader or simply aggregator, is client software or a web application which aggregates syndicated web content such as online newspapers, blogs, podcasts, and video blogs (vlogs) in one location for easy viewing. RSS is a synchronized subscription system. Basically, RSS uses extensible markup language (XML) to structure pieces of information to be aggregated in a feed reader that displays the information in a user-friendly interface. The updates distributed include, for example, journal tables of contents, podcasts, videos, and news items.”

        https://en.wikipedia.org/wiki/News_aggregator


We require a collection of links pointing towards RSS Feeds and Twitter handles. We found a news aggregator Newstral https://newstral.com/de . By scrolling down for several minutes so that it loads much more news sources. we save the HTML so that we can extract the needed information.

Now we extract the valuable information; RSS feeds and Twitter handles. These two different systems give us the possibility of peeking into the news stories of the moment.

Over thousands of different news articles are published in Germany with the intent of informing millions. And fortunately for us, the links are also spread out from various different sources. This ensures neutrality with every news source with a level playing field.

"A regular expression, regex or regexp (sometimes called a rational expression) is, in theoretical computer science and formal language theory, a sequence of characters that define a search pattern. Usually, this pattern is then used by string searching algorithms for "find" or "find and replace" operations on strings.”

        https://en.wikipedia.org/wiki/Regular_expression

We use regular expressions to implement heuristics in order to capture these links.

"Readability is a simple tool that makes reading on the Web more enjoyable by removing the clutter around what you’re reading. Readability is a python port of a ruby port of arc90's readability project. Given a HTML document, it pulls out the main body text and cleans it up.”

https://web.archive.org/web/20090303150113/http://lab.arc90.com//experiments//readability//
https://github.com/buriy/python-readability

"Python is a widely used high-level programming language used for general-purpose programming, created by Guido van Rossum and first released in 1991. An interpreted language, Python has a design philosophy which emphasizes code readability (notably using whitespace indentation to delimit code blocks rather than curly braces or keywords), and a syntax which allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java. The language provides constructs intended to enable writing clear programs on both a small and large scale.”

        https://en.wikipedia.org/wiki/Python_(programming_language)

Although coming from somewhat different backgrounds, these two have the following in common;

They have information of date
They have a title
They have content
Text is published regularly

We will describe both systems separately and then later show how they end up in the same database. 

We begin with RSS Feeds.

Date, title and link are extracted from the XML. Then by following the link, we save the page the RSS feed is pointing to. We extract the main content by using Readability. Readability is a Python library one can use to extract the main text of HTML. Readability employs a statistical model to be able to predict accurately the main text.

"The Hypertext Transfer Protocol (HTTP) is an application protocol for distributed, collaborative, hypermedia information systems. HTTP is the foundation of data communication for the World Wide Web. The GET method requests a representation of the specified resource. Requests using GET should only retrieve data and should have no other effect. This is also true of some other HTTP methods. The W3C has published guidance principles on this distinction, saying, "Web application design should be informed by the above principles, but also by the relevant limitations."

        https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol

"Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching and modifying the parse tree. It commonly saves programmers hours or days of work.”

        https://www.crummy.com/software/BeautifulSoup/bs4/doc/

We now use similar techniques to process Twitter handles.

"Requests is an elegant and simple HTTP library for Python, built for human beings.”

        http://docs.python-requests.org/en/master/


By using Requests, also another Python library we can capture the front HTML of a Twitter user feed. This file is used to extract information by:

Using Beautiful Soup we select Tweets with links and extract the date and link.

We process each tweet by removing the link. We take the tweet as a title.

To extract the main content, we use the similar approach as we did with RSS Feed.

"In computing, JSON sometimes JavaScript Object Notation is an open-standard format that uses human-readable text to transmit data objects consisting of attribute–value pairs. It is the most common data format used for asynchronous browser/server communication, largely replacing XML which is used by Ajax.”

        https://en.wikipedia.org/wiki/JSON

Both of these pipelines will produce the following data:

{
   title: ...
   link: …
   content: …
   day: …
   month: …
   year: …
}

"MongoDB is an open-source, document database designed for ease of development and scaling. MongoDB uses JSON-like documents with schemas. MongoDB is developed by MongoDB Inc. and is free and open-source, published under a combination of the GNU Affero General Public License and the Apache License.”

        https://en.wikipedia.org/wiki/MongoDB
        https://docs.mongodb.com/manual/

We save the JSON data in MongoDB. This allows us to efficiently save and retrieve them later. We had to, however, employ a trick. For some reason a problem may randomly occur when rapidly saving multiple documents in MongoDB at the same time. 


"A file format is a standard way that information is encoded for storage in a computer file. It specifies how bits are used to encode information in a digital storage medium. File formats may be either proprietary or free and may be either unpublished or open.”

        https://en.wikipedia.org/wiki/File_format

Through experimentation we found out that the following is a possible robust and flexible solution:

"Unicode is a computing industry standard for the consistent encoding, representation, and handling of text expressed in most of the world's writing systems. Developed in conjunction with the Universal Coded Character Set (UCS) standard and published as The Unicode Standard, the latest version of Unicode contains a repertoire of more than 128,000 characters covering 135 modern and historic scripts, as well as multiple symbol sets.”

        https://en.wikipedia.org/wiki/Unicode

"UTF-8 is a character encoding capable of encoding all possible characters, or code points, defined by Unicode.”

        https://en.wikipedia.org/wiki/UTF-8

We save the text in a JSON file. The filename will be named by replacing the nonwords characters of the title with underscores and lowercasing all of the characters. An example would be "This Is Where We Are” would be "this_is_where_we_are”. This would avoid any operating system errors from popping up.

This allows us to save the file safely. This is also very flexible because this is a text file. If our MongoDB is broken and unaccessible we still have JSON files which can be read by any other program.

"Ubuntu is a Debian-based Linux operating system for personal computers, tablets, and smartphones, where Ubuntu Touch edition is used; and also runs network servers, usually with the Ubuntu Server edition, either on physical or virtual servers (such as on mainframes) and/or with containers, that is with enterprise-class features; runs on the most popular architectures, including server-class ARM-based.”

        https://en.wikipedia.org/wiki/Ubuntu_(operating_system)

"Redis is an open source (BSD licensed), in-memory data structure store, used as a database, cache and message broker. It supports data structures such as strings, hashes, lists, sets, sorted sets with range queries, bitmaps, hyperlog logs and geospatial indexes with radius queries.”

        https://redis.io/

After successfully saving the JSON file, we push the directory file path in a Redis set. This allows us to continue on the next item without waiting for the write to finish.

Another separate program will have an infinite loop. Each iteration of this loop will pop the Redis set which we saved the directory file paths of JSON files. The JSON file is then read and saved as a document in MongoDB.

At the same time, we index our documents with Elasticsearch. This allows us to retrieve news articles quickly and efficiently.

"Elasticsearch is a search engine based on Lucene. It provides a distributed, multitenant-capable full-text search engine with an HTTP web interface and schema-free JSON documents. Elasticsearch is developed in Java and is released as open source under the terms of the Apache License. Elasticsearch is the most popular enterprise search engine followed by Apache Solr, also based on Lucene. ” 

        https://en.wikipedia.org/wiki/Elasticsearch

"Elasticsearch is a distributed, RESTful search and analytics engine capable of solving a growing number of use cases. As the heart of the Elastic Stack, it centrally stores one's data so one can discover the expected and uncover the unexpected.”

        https://www.elastic.co/products/elasticsearch

"Natural language processing is a field of computer science, artificial intelligence, and computational linguistics concerned with the interactions between computers and human (natural) languages. As such, NLP is related to the area of human–computer interaction. Many challenges in NLP involve: natural language understanding, enabling computers to derive meaning from human or natural language input; and others involve natural language generation.”

        https://en.wikipedia.org/wiki/Natural_language_processing

"Pycld2 contains the Compact Language Detection library as maintained by Dick Sites https://code.google.com/p/cld2/ . It also contains python bindings that were originally created by Mike McCandless. The bindings here differ than upstream by making the full set of languages the default option supporting more than 165 languages.”

        https://github.com/aboSamoor/pycld2

Now we go ahead and start applying Natural Language Processing to mine more information. We first use Pycld2 to detect the language. We save the language information.

"spaCy is an open-source software library for advanced Natural Language Processing, written in the programming languages Python and Cython. It offers the fastest syntactic parser in the world. The library is published under the MIT license and currently supports English and German, as well as tokenization for Chinese and several other languages.”

        https://en.wikipedia.org/wiki/SpaCy

We then use Spacy to do several more extraction. Spacy supports German and English. This is perfect since the languages used in the saved news articles are mostly in German and English.

"Named-entity recognition (NER) (also known as entity identification, entity chunking and entity extraction) is a subtask of information extraction that seeks to locate and classify named entities in text into pre-defined categories such as the names of persons, organizations, locations, expressions of times, quantities, monetary values, percentages, etc.”

        https://en.wikipedia.org/wiki/Named-entity_recognition

So we use Spacy to extract named entity. This process is also known as Named Entity Recognition. Named entities include; people’s name, places, and names of organizations among others. We save each news articles as a list of named entities. The order should be preserved, meaning the first appearing named entity should appear first in the list. Spacy does not retain duplicates. But if they do, it would be a great addition. If not, it would not be that any worse.


Now we use Gensim to do more processing. Gensim has great implementation of topic models which make it easy and practical to use.

"Gensim is a mature open-source vector space modeling and topic modeling toolkit implemented Python. It uses NumPy, SciPy and optionally Cython for performance. It is specifically designed to handle large text collections, using data streaming and efficient incremental algorithms, which differentiates it from most other scientific software packages that only target batch and in-memory processing.”

https://en.wikipedia.org/wiki/Gensim

"Gensim is a free Python library designed to automatically extract semantic topics from documents, as efficiently (computer-wise) and painlessly (human-wise) as possible.”

        https://radimrehurek.com/gensim/intro.html

We query our MongoDB to get the news articles of the current and previous day. We use this to determine which named entities are currently trending.

"In information retrieval, tf–idf, short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus. It is often used as a weighting factor in information retrieval, text mining, and user modeling. The tf-idf value increases proportionally to the number of times a word appears in the document, but is offset by the frequency of the word in the corpus, which helps to adjust for the fact that some words appear more frequently in general. Nowadays, tf-idf is one of the most popular term-weighting schemes. For instance, 83% of text-based recommender systems in the domain of digital libraries use tf-idf.”

        https://en.wikipedia.org/wiki/Tf%E2%80%93idf

We create a tf-idf model using the list of named entities. We score each named entities by summing up the tf idf scores of each named entity.

We pick the first 50 named entities and declare those as trending.

Now we need to present the processed data in a convenient and accessible way.

We can query Elasticsearch and reshape the results so that we get a list of news articles ranked by relevance towards the query. We will design our presentation such that the end user would produce queries consisting of named entities. Our system, however, should not break if it is fed with none named entity queries.

Our search result would consist of a list of Documents which are sorted by time. If the total of results is greater than 50, we truncate it to 50. Now, we need to sort the news articles by date. Now, we use the date as a key to a Python dictionary. We did not use a regular Python dictionary however. We, instead used defaultdict and use list as the default value.

A defaultdict is different to a regular Python dictionary. In that, it has default datatypes. This means that we can use the built-in methods of the datatypes. A list in Python has the append method. We iterate through our list of news articles, each news article is appended to the lists which are values of the defaultdict.

Now we need to clean up our defaultdict. The reason for this is because when a particular date has too many items, the timeline produced would be unreadable or unaesthetic. Therefore, we limit the amount of items per date to four..

"In computing, a hash table (hash map) is a data structure used to implement an associative array, a structure that can map keys to values. Python's built-in hash table implementation, in the form of the dict type, as well as Perl's hash type are used internally to implement namespaces and therefore need to pay more attention to security, i.e., collision attacks. Python sets also use hashes internally, for fast lookup (though they store only keys, not values).”

        https://en.wikipedia.org/wiki/Hash_table

"defaultdict returns a new dictionary-like object. defaultdict is a subclass of the built-in dict class. It overrides one method and adds one writable instance variable. The remaining functionality is the same as for the dict class”

        https://docs.python.org/3.5/library/collections.html#collections.defaultdict

We reshape the dictionary into a JSON which is compatible with Timeline.

We serve this search engine as a Rest API. This Rest API can then be consumed by other applications. In this case, we would use Ruby On Rails.

Ruby on Rails was chosen as the web framework of choice because the ease of prototyping. It is a all-in-one solution for many purposes. In one project we have a database connection, frontend platform and a caching mechanism.

Ruby on Rails will consume the Rest API and serve the functionality as search function on its front-end. The end user will see a search field where one can enter a query.


"In computer programming, an application programming interface (API) is a set of subroutine definitions, protocols, and tools for building application software. In general terms, it's a set of clearly defined methods of communication between various software components. A good API makes it easier to develop a computer program by providing all the building blocks, which are then put together by the programmer. "

        https://en.wikipedia.org/wiki/Application_programming_interface

"Representational state transfer (REST) or RESTful Web services are one way of providing interoperability between computer systems on the Internet. REST-compliant Web services allow requesting systems to access and manipulate textual representations of Web resources using a uniform and predefined set of stateless operations. Other forms of Web service exist, which expose their own arbitrary sets of operations such as WSDL and SOAP.”

        https://en.wikipedia.org/wiki/Representational_state_transfer

"Ruby on Rails is a web application framework optimized for sustainable programming productivity, allows writing sound code by favoring convention over configuration.”
        http://www.dmoz.org/Computers/Programming/Languages/Ruby/Software/Frameworks/Rails/

"Ruby on Rails, or simply Rails, is a server-side web application framework written in Ruby under the MIT License. Rails is a model–view–controller (MVC) framework, providing default structures for a database, a web service, and web pages. It encourages and facilitates the use of web standards such as JSON or XML for data transfer, and HTML, CSS and JavaScript for display and user interfacing. In addition to MVC, Rails emphasizes the use of other well-known software engineering patterns and paradigms, including convention over configuration (CoC), don't repeat yourself (DRY), and the active record pattern.”

        https://en.wikipedia.org/wiki/Ruby_on_Rails

"Database is a usually large collection of data organized especially for rapid search and retrieval (as by a computer)”

        https://www.merriam-webster.com/dictionary/database

"A database is an organized collection of data. It is the collection of schemas, tables, queries, reports, views, and other objects. The data are typically organized to model aspects of reality in a way that supports processes requiring information, such as modelling the availability of rooms in hotels in a way that supports finding a hotel with vacancies.”
w database

        https://en.wikipedia.org/wiki/Database#cite_note-1

"PostgreSQL, often simply Postgres, is an object-relational database (ORDBMS) – i.e. a RDBMS, with additional (optional use) "object" features – with an emphasis on extensibility and standards compliance. As a database server, its primary function is to store data securely, and to allow for retrieval at the request of other software applications. It can handle workloads ranging from small single-machine applications to large Internet-facing applications (or for data warehousing) with many concurrent users; on macOS Server, PostgreSQL is the default database and it is also available for Microsoft Windows and Linux (supplied in most distributions).”

        https://en.wikipedia.org/wiki/PostgreSQL

"PostgreSQL is a powerful, open source object-relational database system. It has more than 15 years of active development and a proven architecture that has earned it a strong reputation for reliability, data integrity, and correctness. "

        https://www.postgresql.org/about/

"TimelineJS or Timeline is an open-source tool that enables anyone to build visually rich, interactive timelines.”
        
        https://timeline.knightlab.com/


We serve the top named entities as trending entities in our frontpage. These entities will be links, when clicked will do the same thing as entering it in the search field.


"Front-end web development, also known as client-side development is the practice of producing HTML, CSS and JavaScript for a website or Web Application so that a user can see and interact with them directly. The challenge associated with front end development is that the tools and techniques used to create the front end of a website change constantly and so the developer needs to constantly be aware of how the field is developing.”

        https://en.wikipedia.org/wiki/Front-end_web_development

The results will be presented in a timeline so that users can investigate how an idea or person evolves through time. This is interesting because sometimes an organization or person will change their stance on different issues.


"Stance can be defined as being in favor or against a defined target such as a controversial topic, e.g. being in favor of atheism or being against it.”

        http://www.ltl.uni-due.de/wp-content/uploads/konvens2016.pdf

"Stance detection is the task of automatically determining from text whether the author of the text is in favor of, against, or neutral towards a proposition or target. The target may be a person, an organization, a government policy, a movement, a product, etc. For example, one can infer from Barack Obama’s speeches that he is in favor of stricter gun laws in the US.”

        https://www.aclweb.org/anthology/S/S16/S16-1003.pdf

Additionally, it would be helpful if the user gets suggestions to the question of: "Which other timelines is related to this current timeline?”

For example, the query "Lufthansa”. A related query would be LH464 which is a flight that gained attention from news.

In order to compute compute related entities, we utilize Word2Vec which is shipped together with Gensim. The model allows us to get similar entities. We choose the seven most similar entities. This allows the user to almost infinitely explore different timelines. 


"Word2vec is a group of related models that are used to produce word embeddings. These models are shallow, two-layer neural networks that are trained to reconstruct linguistic contexts of words. Word2vec takes as its input a large corpus of text and produces a vector space, typically of several hundred dimensions, with each unique word in the corpus being assigned a corresponding vector in the space. Word vectors are positioned in the vector space such that words that share common contexts in the corpus are located in close proximity to one another in the space."

        https://en.wikipedia.org/wiki/Word2vec

"We propose two novel model architectures for computing continuous vector representations of words from very large data sets. The quality of these representations is measured in a word similarity task, and the results are compared to the previously best performing techniques based on different types of neural networks. We observe large improvements in accuracy at much lower computational cost, i.e. it takes less than a day to learn high quality word vectors from a 1.6 billion words data set. Furthermore, we show that these vectors provide state-of-the-art performance on our test set for measuring syntactic and semantic word similarities.”
        
        https://arxiv.org/pdf/1301.3781v3.pdf

To add more information to the timelines we add summary to each particular item of timeline. We employ the PageRank algorithm, also supplied by Gensim to summarize the content to 20 words. This allows the user to know roughly what the main information of the news articles are without visiting or reading the news article itself. If the user is engaged by the description, a link can be clicked and the user will be forwarded to the original content.


"The Gensim module for summarization is based on the popular "TextRank” algorithm and was contributed recently by the good people from the Engineering Faculty of the University in Buenos Aires. This module automatically summarizes the given text, by extracting one or more important sentences from the text. In a similar way, it can also extract keywords.”

        https://rare-technologies.com/text-summarization-with-gensim/

Now we have a nice little tool to use to be able to explore news inside the dimension of time. This is usually a special edition in most news publications but in this system, it is mass produced requires almost no effort. We have successfully built a fun piece of technology that informs and entertains.

http://chronik.herokuapp.com
http://kronologi.herokuapp.com






