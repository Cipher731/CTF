import dis, marshal
from types import CodeType
from opcode import *


def all_interpret(code_obj):
    i = 0
    code = code_obj.co_code
    while 0 <= i < len(code):
        print i
        c = code[i]
        op = ord(c)

        if op >= HAVE_ARGUMENT:
            oparg = ord(code[i + 1]) + ord(code[i + 2]) * 256
            i += 3
            try:
                dis.disassemble_string(code[i - 3: i])
                if op == opmap['LOAD_FAST']:
                    print '\tLocal LOAD [%s]' % code_obj.co_varnames[oparg]
                elif op == opmap['STORE_FAST']:
                    print '\tLocal STORE [%s]' % code_obj.co_varnames[oparg]
                elif op == opmap['LOAD_CONST']:
                    print '\t%s' % code_obj.co_consts[oparg]
                elif op == opmap['STORE_GLOBAL']:
                    print '\tGlobal STORE [%s]' % code_obj.co_names[oparg]
                elif op == opmap['LOAD_GLOBAL']:
                    print '\tGLOBAL LOAD [%s]' % code_obj.co_names[oparg]
            except:
                pass
        else:
            i += 1
            try:
                dis.disassemble_string(code[i - 1: i])
            except:
                pass


def interactive_interpret(code_obj):
    i = 0
    stack = []
    values = {}
    code = code_obj.co_code
    jump = False
    divide = False
    while 0 <= i < len(code):
        try:
            if not jump and not divide:
                ins = raw_input('\n' + str(i))
                if ins.startswith('+'):
                    i += int(ins[1:])
                elif ins.startswith('='):
                    i = int(ins[1:])
            jump = False
            print stack[::-1]
            print values
            c = code[i]
            op = ord(c)
            if op >= HAVE_ARGUMENT:
                oparg = ord(code[i + 1]) + ord(code[i + 2]) * 256
                i += 3
                dis.disassemble_string(code[i - 3: i])
                if op == opmap['JUMP_ABSOLUTE']:
                    i = oparg
                    jump = True
                elif op == opmap['JUMP_FORWARD']:
                    i += oparg
                    jump = True
                elif op == opmap['LOAD_FAST']:
                    stack.append(values.get(code_obj.co_varnames[oparg], code_obj.co_varnames[oparg]))
                    print '\tLocal LOAD [%s]' % code_obj.co_varnames[oparg]
                elif op == opmap['STORE_FAST']:
                    if code_obj.co_varnames[oparg] == 'DIVIDER':
                        divide = True
                    values[code_obj.co_varnames[oparg]] = stack.pop()
                    print '\tLocal STORE [%s]' % code_obj.co_varnames[oparg]
                elif op == opmap['LOAD_CONST']:
                    stack.append(code_obj.co_consts[oparg])
                    print '\t%s' % code_obj.co_consts[oparg]
                elif op == opmap['STORE_GLOBAL']:
                    values[code_obj.co_names[oparg]] = stack.pop()
                    print '\tGlobal STORE [%s]' % code_obj.co_names[oparg]
                elif op == opmap['LOAD_GLOBAL']:
                    stack.append(values.get(code_obj.co_names[oparg], code_obj.co_names[oparg]))
                    print '\tGLOBAL LOAD [%s]' % code_obj.co_names[oparg]
                elif op == opmap['COMPARE_OP']:
                    result = eval("%s%s%s" % (stack.pop(), cmp_op[oparg], stack.pop()))
                    stack.append(result)
                elif op == opmap['POP_JUMP_IF_TRUE'] and stack.pop():
                    divide = False
                    i = oparg
                    jump = True
                elif op == opmap['POP_JUMP_IF_FALSE'] and not stack.pop():
                    divide = False
                    i = oparg
                    jump = True
                elif op == opmap['LOAD_ATTR']:
                    stack.append(stack.pop() + '.' + code_obj.co_names[oparg])
                elif op == opmap['CALL_FUNCTION']:
                    ret = []
                    for _ in range(oparg + 1):
                        ret.append(str(stack.pop()))
                    stack.append('%s(%s)' % (ret[-1], ', '.join(ret[-2::-1])))
                elif op == opmap['FOR_ITER']:
                    exhausted = raw_input('=====Exhausted? (y/n)=====') == 'y'
                    if exhausted:
                        stack.pop()
                        i += oparg
                    else:
                        stack.append('iter_value')
                elif op == opmap['BUILD_SLICE']:
                    ret = []
                    for _ in range(oparg):
                        ret.append(str(stack.pop()))
                    stack.append('[%s]' % ':'.join(ret))
                elif op == opmap['IMPORT_NAME']:
                    stack.pop()
                    stack.pop()
                    stack.append(code_obj.co_names[oparg])
                    print 'Import:: %s' % code_obj.co_names[oparg]
                elif op == opmap['STORE_NAME']:
                    values[code_obj.co_names[oparg]] = stack.pop()
                    print '\tName STORE [%s]' % code_obj.co_names[oparg]
                elif op == opmap['LOAD_NAME']:
                    stack.append(values.get(code_obj.co_names[oparg], code_obj.co_names[oparg]))
                    print '\tName LOAD [%s]' % code_obj.co_names[oparg]

            else:
                i += 1
                if op == opmap['PRINT_ITEM']:
                    print 'PRINT: %s' % stack.pop()
                elif op == opmap['POP_TOP']:
                    stack.pop()
                elif op == opmap['GET_ITER']:
                    stack.append('iter(%s)' % stack.pop())
                elif opname[op].startswith('BINARY'):
                    stack.append('%s(%s, %s)' % (opname[op], stack.pop(), stack.pop()))
                elif op == opmap['INPLACE_ADD']:
                    stack.append('%s + %s' % (stack.pop(), stack.pop()))
                elif op == opmap['SLICE+3']:
                    ret = []
                    for _ in range(3):
                        ret.append(stack.pop())
                    stack.append('%s[%d:%d]' % (ret[-1], ret[-2], ret[-3]))
                dis.disassemble_string(code[i - 1: i])
        except:
            pass


if __name__ == '__main__':
    f = open('./crackme.pyc', 'rb')
    f.seek(8)
    all_code = marshal.load(f)
    funcs = []
    for const_name in all_code.co_consts:
        if isinstance(const_name, CodeType):
            funcs.append(const_name)

    interactive_interpret(funcs[0])
