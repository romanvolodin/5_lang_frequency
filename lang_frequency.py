import argparse
import string


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_data',
                        help='path to bars data in json format',
                        type=str)
    parser.add_argument('--count',
    	                help='total count of the most frequent words '
    	                '(default: 10)',
    	                default=10,
    	                type=int)
    return parser.parse_args()


def load_data(filepath):
    with open(filepath, 'r', encoding='utf-8') as input_file:
    	return input_file.read()


def get_most_frequent_words(text):
    words_frequency = {}
    for word in text.split():
    	word = word.lower()
    	if word in words_frequency.keys():
    		words_frequency[word] += 1
    	else:
    		words_frequency[word] = 1
    return sorted(words_frequency.items(),
    	          key=lambda x: x[1],
    	          reverse=True)


def only_alpha_and_spaces(text):
	return ''.join(char for char in text 
		           if (char.isalpha() or char.isspace())
		           )


if __name__ == '__main__':
    args = parse_arguments()
    path = args.input_data
    count = args.count

    text = load_data(path)
    text = only_alpha_and_spaces(text)
    most_frequent_words = get_most_frequent_words(text)
    
    for zopa in most_frequent_words[:count]:
    	word, count = zopa
    	print('{:>5} {}'.format(count, word))

