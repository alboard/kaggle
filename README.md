My stuckness (congitive function aside) with the RecSys is while I can find, run and edit numerous models that use movie, user and rating numbers models that used categorical or free text not so much - if they do use it they don't create evaluateable models - they just do cosine similarity based lists?  
Yes, need to sweat through the examples that go into the weeds with the text ...
This is close - need to unpick the MS recommender part though - https://github.com/jreynolds01/Recommenders/blob/master/notebooks/00_quick_start/wide_deep_movielens.ipynb

What I had hoped to do was feed a deep learning model with one-hot encoded categorical and Doc2Vec or Word2Vec vectorised single field binary soup of the rest - with bonus points for importing and using promotional movie images as metadata :-)

# RHRN
https://github.com/keras-team/keras-io/blob/0be9a38b96e8dd85bc525a74babb614f38b179c7/examples/structured_data/movielens_recommendations_transformers.py
- but Keras now part of not external to TF - problem?
https://github.com/jreynolds01/Recommenders/blob/master/notebooks/00_quick_start/wide_deep_movielens.ipynb
- unpick the MS recommender part

# Notes
* What I wanted to do was NLP generate from comments, clone,  no-code, low code, Python framework a Notebook that met the requirement of a creating, evaluating, pickling and loading a model trained using movie lens ratings (users, movies, ratings + text metadata), save that as a Python script and overlay the Fire CLI load, task boilerplate on that - then with that attributed exploit in the bank explore and improve - relax and develop calmly as I had working code that met the spec fully - if simply.
* I failed to exploit as I could not find a fully suitable clone or environment in GitHub (should have tried GitLab and model zoo's too), Kaggle, or Medium 
* Did find Google and Microsoft recommenders and papers with code and other notebooks using a slightly different version of movie lens data set - did grok fast that a few simply renames of the actual dataset made these reusable - noted could have used Azure ML studio and completed the task with drag, drop & fill in the box but not saved that as Python script readily ...
* The Python recommendation libraries (e.g. Surprise) did all but the text part of the task in a few lines but extending them looked gnarly …

# Other approaches to try:-
* Google
  * Sorted search
* fast.ai
 * Tabular or collab?
* Python Recsys library
  * Old and cold?  
* scikit-learn
  * Supports text
	*XG Boost?
  	* Surprise?
* Turi Create
* Vowpal Wabbit 
