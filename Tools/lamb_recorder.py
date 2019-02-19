import requests
import cmd
import pickle
import os
import urllib.parse


class Tamper:

    @staticmethod
    def space2comment(pay: str):
        return pay.replace(' ', '/***/')

    @staticmethod
    def union2(pay: str):
        return pay.replace('union', 'ununionion')

    @staticmethod
    def where2(pay: str):
        return pay.replace('where', 'whewherere')

    @staticmethod
    def select2(pay: str):
        return pay.replace('select', 'selselectect')

    @staticmethod
    def order2(pay: str):
        return pay.replace('order', 'oorderrder')

    @staticmethod
    def or2(pay: str):
        return pay.replace('or', 'oorr')

    @staticmethod
    def from2(pay: str):
        return pay.replace('from', 'frfromom')

    @staticmethod
    def load_file2(pay: str):
        return pay.replace('load_file', 'loaload_filed_file')


class Recorder(cmd.Cmd):
    PATH = os.path.dirname(os.path.abspath(__file__)) + '/db/'
    prompt = '(CyberImp) '

    def __init__(self):
        super().__init__()
        self.history = []
        self.note = []
        self.config = {
            'name': '',
            'url': '',
            'tamper': set(),
            'params': {},
            'data': {},
            'target_param': '',
            'cookies': {},
            'headers': {},
            'method': 'get',
            'autosave': False
        }

    def __getstate__(self):
        return {
            'history': self.history,
            'note': self.note,
            'config': self.config
        }

    def __setstate__(self, state):
        self.history = state['history']
        self.note = state['note']
        self.config = state['config']

    def autosave(self):
        if self.config['autosave']:
            if self.config['name']:
                with open(self.PATH + self.config['name'] + '_auto', 'wb') as file:
                    pickle.dump(self, file)
                print('Autosaved.')
            else:
                print('Autosave is turned on but no session name is given.')

    @staticmethod
    def need_args(size):
        print(f"Arguments length is not correct. Expected {size}.")

    @staticmethod
    def too_many_args():
        print("More argument(s) is needed.")

    @staticmethod
    def do_EOF(line):
        raise EOFError()

    def do_set(self, args: str):
        args = args.split(maxsplit=1)
        if len(args) < 2:
            self.need_args(2)
            return

        target = args[0]
        value = args[1]

        if target == 'url':
            c = urllib.parse.urlparse(value)
            if not c.scheme or not c.netloc:
                print('Wrong URL is input. Please check.')
                return

            if c.query:
                p = urllib.parse.parse_qs(c.query)
                self.config['params'].update(p)
                print('Params found.\n{} {} added to params.'.format(', '.join(list(p.keys())),
                                                                     'are' if len(p.keys()) > 1 else 'is'))
            self.config['url'] = value.rstrip(f'?{c.query}')
        elif target == 'method':
            self.config['method'] = value
        elif target == 'param':
            value = value.split(maxsplit=1)
            k = value[0]
            if len(value) == 1:
                self.config['params'][k] = ''
            else:
                v = value[1]
                self.config['params'][k] = v
        elif target == 'data':
            value = value.split(maxsplit=1)
            k = value[0]
            if len(value) == 1:
                self.config['data'][k] = ''
            else:
                v = value[1]
                self.config['data'][k] = v
        elif target == 'cookies':
            k = value.split()[0]
            v = value.split()[1]
            self.config['cookies'][k] = v
        elif target == 'headers':
            k = value.split()[0]
            v = value.split()[1]
            self.config['headers'][k] = v
        elif target == 'target':
            if value in self.config['params'] and self.config['method'] == 'get':
                self.config['target_param'] = value
            elif value in self.config['data'] and self.config['method'] == 'post':
                self.config['target_param'] = value
            else:
                print(f'{value} is not in params/data')
        elif target == 'name':
            self.config['name'] = value
        else:
            print('No such action.')

        print(f'{target} {value} is set.')
        self.autosave()

    @staticmethod
    def complete_set(text, line, begin, end):
        targets = ['url', 'method', 'param', 'cookies', 'headers', 'target', 'name']
        return [target for target in targets if target.startswith(text)]

    def do_config(self, args):
        print('==============================')
        for k in self.config.keys():
            print('{}: {}'.format(k.upper(), self.config.get(k)))
        print('==============================')

    def do_history(self, arg: str):
        if arg == 'all':
            print(f'In total {len(self.history)} history:')
        else:
            print(f'Show recent {5 if len(self.history) > 5 else len(self.history)} history:')

        for index, payload in enumerate(self.history[(0 if arg == 'all' else -5):]):
            print(f'History {index}: {payload}')

    def do_tamper(self, args: str):
        args = args.split(maxsplit=1)
        if len(args) < 1:
            print('Please specify the action.')
            return

        action = args[0]
        if action in ['add', 'remove'] and len(args) < 2:
            self.need_args(2)
            return

        if action == 'add':
            try:
                getattr(Tamper, args[1])
                self.config['tamper'].add(args[1])
            except AttributeError:
                print('No such tamper.')
        elif action == 'show':
            print(list(self.config['tamper']))
        elif action == 'clear':
            self.config['tamper'].clear()
            print("Tamper set cleared.")
        elif action == 'remove':
            try:
                self.config['tamper'].remove(args[1])
            except KeyError:
                print('No such tamper in tamper set.')
        else:
            print('No such action.')

        self.autosave()

    def complete_tamper(self, text, line, begin, end):
        args = ['add', 'remove', 'show', 'clear']
        tampers = [func for func in dir(Tamper) if callable(getattr(Tamper, func)) and not func.startswith('__')]
        line = line.split()
        action = line[1]
        if len(line) <= 2 and action not in args:
            return [arg for arg in args if arg.startswith(text)]

        if action == 'add':
            if text != 'add':
                return [t for t in tampers if t.startswith(text)]
            else:
                return tampers
        if action == 'remove':
            if text != 'remove':
                return [t for t in self.config['tamper'] if t.startswith(text)]
            else:
                return self.config['tamper']

    def do_send(self, payload: str):
        if not self.config['target_param']:
            print('Please specify the target param.')
            return

        params = self.config['params'].copy()
        data = self.config['data'].copy()

        payload = payload.strip()
        if payload.startswith('\'') and payload.endswith('\''):
            payload = payload[1:-1]

        self.history.append(payload)

        for tamper in self.config['tamper']:
            t = getattr(Tamper, tamper)
            payload = t(payload)

        if self.config['method'].lower() == 'get':
            if payload:
                params[self.config['target_param']] = payload
            req = requests.get(self.config['url'],
                               params=params, cookies=self.config['cookies'], headers=self.config['headers'])
            if req.status_code == 200:
                print(req.text)
            else:
                print(req.status_code)
        else:
            if payload:
                data[self.config['target_param']] = payload
            req = requests.post(self.config['url'], params=params,
                                data=data, cookies=self.config['cookies'], headers=self.config['headers'])
            if req.status_code == 200:
                print(req.text)
            else:
                print(req.status_code)

        self.autosave()

    def complete_send(self, text, line, begin, end):
        line = line.split(maxsplit=1)
        total_text = line[1].strip('\'')
        offset = len(total_text) - len(text)
        return [h[offset:] for h in self.history if h.startswith(total_text)]

    def do_note(self, args: str):
        args = args.split(maxsplit=1)
        action = args[0]
        if action == 'add':
            self.note.append(args[1])
        elif action == 'remove':
            del self.note[int(args[1])]
        elif action == 'show':
            for index, note in enumerate(self.note):
                print(f'Note {index}: {note}')
        elif action == 'clear':
            self.note.clear()
        else:
            print('No such action.')

        self.autosave()

    @staticmethod
    def complete_note(text, line, begin, end):
        args = ['add', 'remove', 'show', 'clear']
        line = line.split()
        if len(line) <= 2:
            return [arg for arg in args if arg.startswith(text)]
        return args

    def do_save(self, name: str):
        if not name:
            print('Target file\'s name is not given.')
            if self.config['name']:
                print('Save by its name {}'.format(self.config['name']))
                self.do_save(self.config['name'])
            else:
                print('Current session name is not given either. Action aborted.')
        else:
            with open(self.PATH + name, 'wb') as file:
                pickle.dump(self, file)
                print('{} is saved.'.format(name))

    def complete_save(self, text, line, begin, end):
        return [file for file in os.listdir(self.PATH) if file.startswith(text)]

    def do_autosave(self, args):
        if args == 'on':
            self.config['autosave'] = True
        elif args == 'off':
            self.config['autosave'] = False
        else:
            print('Please specify on/off.')

    @staticmethod
    def complete_autosave(text, line, begin, end):
        return [opt for opt in ['on', 'off'] if opt.startswith(text)]

    def do_load(self, name):
        if not name:
            print('Target file\'s name is not given.')
        else:
            with open(self.PATH + name, 'rb') as file:
                obj = pickle.load(file)
                self.__setstate__(obj.__getstate__())
                print('{} is loaded.\nBelow are configuration.'.format(name))
                self.do_config('')

    def complete_load(self, text, line, begin, end):
        return [file for file in os.listdir(self.PATH) if file.startswith(text)]

    def do_quit(self, line):
        return self.do_EOF(line)


if __name__ == '__main__':
    r = Recorder()
    while True:
        try:
            r.cmdloop()
        except (EOFError, KeyboardInterrupt):
            break
        except Exception as e:
            print("Error:", e)
