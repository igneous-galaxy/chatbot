from random import shuffle


class Test:
    def __init__(self, test):
        self.test = test['test']
        self.count = -1
        self.result = 0
        order = list(range(0, len(test)))
        shuffle(order)
        self.order = order[:10]

    def ask_next(self):
        self.count += 1
        current = self.test[self.count]

        res = {}

        if 'answers' in current:
            res['text'] = '❔  ' + current['question']
            res['markup'] = current['answers']

        else:
            res['text'] = current['task'] + '\n\n❔  ' + current['question']
            res['markup'] = None

        res['count'] = self.count + 1

        return res

    def check_it(self, answer):
        if answer == self.test[self.count]['response']:
            self.result += 1

    def get_result(self):
        return self.result

