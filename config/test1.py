{
 "cells": [
  {
   "cell_type": "coabde",
   "execution_count": null,
   "metadata": {},
   "test":{tset}
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream1",
     "text": [
      "Hi, this is saiteja and he is gopi\n"
     ]
    }
   ],
   "source": [
    "# print(\"Hi, this is %s and he is %s\"%('saiteja','gopi'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'tensorflow'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-64156d691fe5>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mtensorflow\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mtf\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'tensorflow'"
     ]
    }
   ],
   "source": [
    "import tensorflow as tf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "My name is Vamsi and my mother name is Radha\n"
     ]
    }
   ],
   "source": [
    "print(\"My name is %s and my mother name is %s\"%('Vamsi','Radha'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hi, this is ravi and he is raju\n"
     ]
    }
   ],
   "source": [
    "x='ravi'\n",
    "y='raju'\n",
    "print(\"Hi, this is %s and he is %s\"%(x,y))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "First: hi!, Second:  3.14, Third: 'bye!'\n"
     ]
    }
   ],
   "source": [
    "print('First: %s, Second: %5.2f, Third: %r' %('hi!',3.1415,'bye!'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world! my name is vaseekar\n"
     ]
    }
   ],
   "source": [
    "print(\"hello world! my name is {}\".format('vaseekar'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello i am saiteja my age is 24\n"
     ]
    }
   ],
   "source": [
    "print('hello i am {} my age is {}'.format('saiteja',24))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 86,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Left                 |        Center       |                Right \n"
     ]
    }
   ],
   "source": [
    "print('{0:<20} | {1:^20}| {2:>20} '.format('Left','Center','Right'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=['a','b','c']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=[1,2,3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 2, 3]"
      ]
     },
     "execution_count": 95,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x[0]*2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 115,
   "metadata": {},
   "outputs": [],
   "source": [
    "x_dict={'key1':123,'key2':[1,2,3],'key3':['a','b','c']}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 118,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "123"
      ]
     },
     "execution_count": 118,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_dict['key1']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 120,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 120,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_dict['key2'][2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 122,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_keys(['key1', 'key2', 'key3'])"
      ]
     },
     "execution_count": 122,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_dict.keys()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 123,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_values([123, [1, 2, 3], ['a', 'b', 'c']])"
      ]
     },
     "execution_count": 123,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_dict.values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 124,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "dict_items([('key1', 123), ('key2', [1, 2, 3]), ('key3', ['a', 'b', 'c'])])"
      ]
     },
     "execution_count": 124,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_dict.items()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 125,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'key1': 123, 'key2': [1, 2, 3], 'key3': ['a', 'b', 'c']}"
      ]
     },
     "execution_count": 125,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x_dict"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 126,
   "metadata": {},
   "outputs": [],
   "source": [
    "t_tuple=('a',1,2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "('a', 1, 2)"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t_tuple"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 135,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "t_tuple.index(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 150,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=set()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 151,
   "metadata": {},
   "outputs": [],
   "source": [
    "x.add(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 152,
   "metadata": {},
   "outputs": [],
   "source": [
    "x.add(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 153,
   "metadata": {},
   "outputs": [],
   "source": [
    "x.add(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 156,
   "metadata": {},
   "outputs": [],
   "source": [
    "x.add(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 158,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{1, 2, 3}"
      ]
     },
     "execution_count": 158,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overwriting abc.txt\n"
     ]
    }
   ],
   "source": [
    "%%writefile abc.txt\n",
    "Hey, This is Saiteja Boyapati.\n",
    "I am doing great.\n",
    "How are you doing."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 179,
   "metadata": {},
   "outputs": [],
   "source": [
    "abc=open('abc.txt')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 192,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 192,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "abc.seek(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 193,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Hey, This is Saiteja Boyapati.\\n',\n",
       " 'I am doing great.\\n',\n",
       " 'How are you doing.']"
      ]
     },
     "execution_count": 193,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "abc.readlines()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 195,
   "metadata": {},
   "outputs": [],
   "source": [
    "abc.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 202,
   "metadata": {},
   "outputs": [],
   "source": [
    "abc=open('abc.txt','+w')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 203,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "19"
      ]
     },
     "execution_count": 203,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "abc.write('Hey It got deleted.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 204,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hey It got deleted.'"
      ]
     },
     "execution_count": 204,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "abc.seek(0)\n",
    "abc.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 206,
   "metadata": {},
   "outputs": [],
   "source": [
    "abc=open('abc.txt','+a')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 207,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "39"
      ]
     },
     "execution_count": 207,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "abc.write('Hello this is added to the previous one')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 212,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Hey It got deleted.Hello this is added to the previous one'"
      ]
     },
     "execution_count": 212,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "abc.seek(0)\n",
    "abc.read()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "metadata": {},
   "outputs": [],
   "source": [
    "abc.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[1, 4, 7, 10, 13, 16, 19]"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "list(range(1,20,3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a value:gau\n",
      "the value is:gau\n"
     ]
    }
   ],
   "source": [
    "a=input('enter a value:')\n",
    "print('the value is:{}'.format(a))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "a=[x for x in range(25) if x%2==0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "def primenum(num):\n",
    "    for numb in range(2,num):\n",
    "        if numb%2==0:\n",
    "            print('{} is not a prime number'.format(num))\n",
    "            break\n",
    "    else:\n",
    "        print('{} is a prime number'.format(num))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2 is a prime number\n"
     ]
    }
   ],
   "source": [
    "primenum(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "rev=lambda s: s[::-1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'olleh'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "rev('hello')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "a=[1,3,4,5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.pop(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4, 5]"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4, 5, 1, 1, 1]"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.append(1)\n",
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "a.append(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4, 1, 5, 1]"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.pop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[3, 4, 1, 5]"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=list(range(3,3,2))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[]"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x=[num for num in range(0,10)]\n",
    "x\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "2\n",
      "2 2 5\n",
      "2 6 9\n",
      "NO\n",
      "2\n",
      "1 5 8 \n",
      "3 5 6\n",
      "NO\n"
     ]
    }
   ],
   "source": [
    "t=int(input())\n",
    "for i in range(0,t):\n",
    "    n=int(input())\n",
    "    sum=0\n",
    "    l=[0 for i in range(0,4001)]\n",
    "    for i in range(0,n):\n",
    "        x,y,h=[int(i) for i in input().split()]\n",
    "        l[x-y+2000]+=h \n",
    "        sum+=h \n",
    "    cur=0\n",
    "    yes=0\n",
    "    for i in range(0,4001):\n",
    "        cur+=l[i]\n",
    "        if ((sum%2 ==0) and (cur==(sum-cur))):\n",
    "            yes=1\n",
    "            break\n",
    "        if ((sum%2==(l[i]%2)) and (cur-l[i]==(sum-cur))):\n",
    "            yes=1\n",
    "            break\n",
    "    if yes:\n",
    "        print(\"YES\")\n",
    "    else:\n",
    "        print(\"NO\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Robot:\n",
    "    def __init__(self,name,color,age):\n",
    "        self.name=name\n",
    "        self.color=color\n",
    "        self.age=age\n",
    "    def x(self):\n",
    "        print('name {}\\nage {}\\ncolor {}'.format(self.name,self.age,self.age))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [],
   "source": [
    "r1=Robot('tom','white',23)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "name tom\n",
      "age 23\n",
      "color 23\n"
     ]
    }
   ],
   "source": [
    "r1.x()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "9\n",
      "abcdefghi\n",
      "i\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "l=input()\n",
    "maxs=l[0]\n",
    "s=l[0]\n",
    "check=l[0]\n",
    "for i in range(1,n):\n",
    "        if ord(check) >= ord(l[i]):\n",
    "            s=s+l[i]\n",
    "        else:\n",
    "            check=l[i]\n",
    "            s=l[i]\n",
    "        if (ord(s[0]) >= ord(maxs[0])):\n",
    "            maxs=s\n",
    "    \n",
    "print(maxs)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "a='fjldj'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['fjldj']"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "a.split()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter no of digits2\n",
      "enter string:hgjdfojdfslakjlgj\n",
      "hg\n"
     ]
    }
   ],
   "source": [
    "from sys import stdin, stdout\n",
    "n = int(input('enter no of digits'))\n",
    "s = input('enter string:')\n",
    "arr = []\n",
    "for i in range(n):\n",
    "\tarr.append(s[i:n])\n",
    "arr.sort()\n",
    "stdout.write( arr[len(arr) - 1] + \"\\n\" )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25\n",
      "[0, 0, 0, 1, 1, 2, 4, 8, 15, 29, 56, 108, 208, 401, 773, 1490, 2872, 5536, 10671, 20569, 39648, 76424, 147312, 283953, 547337]\n",
      "1137418\n"
     ]
    }
   ],
   "source": [
    "import sys\n",
    "import math\n",
    "from sys import stdin, stdout\n",
    "\n",
    "# Auto-generated code below aims at helping you parse\n",
    "# the standard input according to the problem statement.\n",
    "\n",
    "n = int(input())\n",
    "a,b,c,d,e=0,0,0,1,1\n",
    "lst=[a,b,c,d]\n",
    "for i in range(4,n):\n",
    "    x=a+b+c+d\n",
    "    lst.append(x) \n",
    "    a=b\n",
    "    b=c\n",
    "    c=d\n",
    "    d=x\n",
    "z=sum(lst)\n",
    "print(lst)\n",
    "print(z)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "1 2 3 5\n",
      "3\n",
      "1 3\n",
      "10\n",
      "2 5\n",
      "8\n",
      "2 20\n",
      "8\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "a = []\n",
    "for i in input().split():\n",
    "    x = int(i)\n",
    "    a.append(x)\n",
    "m = int(input())\n",
    "for i in range(m):\n",
    "    s, e = [int(j) for j in input().split()]\n",
    "    x = sum(a[s:e+1])\n",
    "    print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hai how r u\n"
     ]
    },
    {
     "ename": "IndexError",
     "evalue": "list index out of range",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mIndexError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-53-e582cc82c02a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      9\u001b[0m             \u001b[0mcount\u001b[0m\u001b[1;33m=\u001b[0m \u001b[0mcount\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     10\u001b[0m             \u001b[1;32mbreak\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 11\u001b[1;33m         \u001b[1;32melif\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mj\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mm\u001b[0m\u001b[1;33m)\u001b[0m \u001b[1;32mand\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m[\u001b[0m\u001b[0mj\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m \u001b[1;32min\u001b[0m \u001b[0mm\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     12\u001b[0m             \u001b[0mcount\u001b[0m\u001b[1;33m=\u001b[0m \u001b[0mcount\u001b[0m\u001b[1;33m+\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     13\u001b[0m             \u001b[1;32mbreak\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mIndexError\u001b[0m: list index out of range"
     ]
    }
   ],
   "source": [
    "s = input()\n",
    "count=0\n",
    "l=['a','e','i','o','u']\n",
    "lst1=s.split()\n",
    "for i in range(len(lst1)):\n",
    "    x=list(lst1[i])\n",
    "    for j in range(len(x)):\n",
    "        if (x[j] in l) and (x[j+1] in l):\n",
    "            count= count+1\n",
    "            break\n",
    "        elif(x[j] in m) and (x[j+1] in m):\n",
    "            count= count+1\n",
    "            break\n",
    "                \n",
    "        else:\n",
    "            continue\n",
    "print(count)\n",
    "              \n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "127.0.0.58\n",
      "['1', '2', '7', '.', '0', '.', '0', '.', '5', '8']\n",
      "['1', '2', '7', '0', '0', '5', '8']\n",
      "[1, 2, 7, 0, 0, 5, 8]\n",
      "the ip address is: 127.0.0.58\n",
      "port no is: 23\n"
     ]
    }
   ],
   "source": [
    "ip=input()\n",
    "lst=list(ip)\n",
    "print(lst)\n",
    "x='.'\n",
    "while x in lst:\n",
    "    lst.remove('.')\n",
    "print(lst)\n",
    "lst=list(map(int,lst))\n",
    "print(lst)\n",
    "print('the ip address is: {}'.format(ip))\n",
    "x=sum(lst)\n",
    "port=x*lst[0]\n",
    "print('port no is: {}'.format(port))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "128"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sum(lst)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5\n",
      "1\n",
      "22\n",
      "333\n",
      "4444\n",
      "55555\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "for i in range(1,n+1):\n",
    "    print(str(i)*i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "l=[]\n",
    "prime=[]\n",
    "for i in range(n):\n",
    "    m = int(input())\n",
    "    l.append(m)\n",
    "for i in l:\n",
    "    for x in range (2,i):\n",
    "        if (i % x) == 0:\n",
    "            break\n",
    "    else:\n",
    "        prime.append(i)\n",
    "print(max(prime))\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "1\n",
      "3\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "lst=[]\n",
    "for i in range(1,n+1):\n",
    "    print (i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4 5 2\n",
      "1 4 5 3 2\n",
      "1 4 3 2 "
     ]
    }
   ],
   "source": [
    "i = [int(x) for x in input().split()]\n",
    "n,m,d = i[0],i[1],i[2]\n",
    "a = [int(x) for x in input().split()]\n",
    "lst = sorted(a,key=int,reverse=True)\n",
    "lst1 = lst[0:m-n]\n",
    "for i in a:\n",
    "    if i not in lst1:\n",
    "        print(i, end=' ')\n",
    "    else:\n",
    "        continue\n",
    "\n",
    "    \n",
    "    \n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "1 6 3 2 5 1 \n",
      "10\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "p=[int(x) for x in input().split()]\n",
    "counter=0\n",
    "for i in range(n):\n",
    "    for j in range(i+1,n):\n",
    "        for k in range(i,n):\n",
    "            if ((p[i]+p[j]) >= p[k] and abs(p[i]-p[j]) <= p[k]):\n",
    "                if (p[i]+p[k] >= p[j] and p[j]+ p[k] >= p[i] and abs(p[i]-p[k]) >= p[j] and abs(p[j]+ p[k]) >= p[i]):\n",
    "                    counter=counter+1\n",
    "        else:\n",
    "            continue\n",
    "print(counter)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "1 6 3 2 5 1\n"
     ]
    }
   ],
   "source": [
    "n=int(input())\n",
    "p=[int(x) for x in input().split()]\n",
    "counter=0\n",
    "lst=[]\n",
    "for i in range(n):\n",
    "    for j in range(i,n):\n",
    "        lst.append((p[i],p[j]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(1, 1),\n",
       " (1, 6),\n",
       " (1, 3),\n",
       " (1, 2),\n",
       " (1, 5),\n",
       " (1, 1),\n",
       " (6, 6),\n",
       " (6, 3),\n",
       " (6, 2),\n",
       " (6, 5),\n",
       " (6, 1),\n",
       " (3, 3),\n",
       " (3, 2),\n",
       " (3, 5),\n",
       " (3, 1),\n",
       " (2, 2),\n",
       " (2, 5),\n",
       " (2, 1),\n",
       " (5, 5),\n",
       " (5, 1),\n",
       " (1, 1)]"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lst"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 1 1\n",
      "1 6 6\n",
      "1 3 3\n",
      "1 2 1\n",
      "1 5 6\n",
      "1 1 1\n",
      "6 6 1\n",
      "6 3 6\n",
      "6 2 6\n",
      "6 5 1\n",
      "6 1 6\n",
      "3 3 1\n",
      "3 2 1\n",
      "3 5 6\n",
      "3 1 3\n",
      "2 2 1\n",
      "2 5 6\n",
      "2 1 1\n",
      "5 5 1\n",
      "5 1 6\n",
      "1 1 1\n",
      "21\n"
     ]
    }
   ],
   "source": [
    "def triangle(abc):\n",
    "    global counter\n",
    "    for x,y in abc:\n",
    "        for z in p:\n",
    "            if (((x+y)>=z) and ((y+z) >=x) and ((x+z)>=y) and (abs(x-y)<=z) and (abs(y-z) <=x) and (abs(x-z)<=y)):\n",
    "                counter=counter+1\n",
    "                print(x,y,z)\n",
    "                break\n",
    "            else:\n",
    "                continue\n",
    "    return counter\n",
    "triangle(lst)\n",
    "print(counter)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 1\n",
      "1 6\n",
      "1 3\n",
      "1 2\n",
      "1 5\n",
      "1 1\n",
      "6 6\n",
      "6 3\n",
      "6 2\n",
      "6 5\n",
      "6 1\n",
      "3 3\n",
      "3 2\n",
      "3 5\n",
      "3 1\n",
      "2 2\n",
      "2 5\n",
      "2 1\n",
      "5 5\n",
      "5 1\n",
      "1 1\n"
     ]
    }
   ],
   "source": [
    "for x,y in lst:\n",
    "    print(x,y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2123\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "print(sum((k+1)%2*k for k in map(int,input())))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n",
      "['olleH', 'dlroW']\n",
      "olleH dlroW\n"
     ]
    }
   ],
   "source": [
    "s = input().split()\n",
    "\n",
    "for i in range(len(s)):\n",
    "    s[i]=s[i][::-1]\n",
    "print(s)\n",
    "print(' '.join(s))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hai How Are You\n",
      "['Hai', 'How', 'Are', 'You']\n",
      "Hai\n",
      "How\n",
      "Are\n",
      "You\n"
     ]
    }
   ],
   "source": [
    "x=input().split()\n",
    "print(x)\n",
    "print('\\n'.join(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 85,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hello World\n",
      "olleH dlroW "
     ]
    }
   ],
   "source": [
    "s = input()\n",
    "for word in s.split():\n",
    "    print(word[::-1],end=' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "13:5\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "785"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "h,m=map(int,input().split(':'))\n",
    "h*60+m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 104,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "LJLFJJ\n"
     ]
    }
   ],
   "source": [
    "s=input()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'ljlfjj'"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "s.lower()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "65"
      ]
     },
     "execution_count": 101,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ord('A')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "122"
      ]
     },
     "execution_count": 107,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ord('z')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hai Vinay\n",
      "hAI vINAY"
     ]
    }
   ],
   "source": [
    "s = input()\n",
    "for i in s:\n",
    "    if ord(i) in range(65,97):\n",
    "        print(i.lower(),end='')\n",
    "    elif ord(i) in range(97,123):\n",
    "        print(i.upper(),end='')\n",
    "    else:\n",
    "        print(i,end='')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 117,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Hai how are You?\n",
      "hAI HOW ARE yOU?"
     ]
    }
   ],
   "source": [
    "s=input()\n",
    "for i in s:\n",
    "    if i.isupper():\n",
    "        print(i.lower(),end='')\n",
    "    else:\n",
    "        print(i.upper(),end='')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 135,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "true\n",
      "false\n",
      "true\n",
      "false\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "x=[]\n",
    "for i in range(n):\n",
    "    x.append(int(input()))\n",
    "for i in x:\n",
    "    if i%2==0:\n",
    "        print('true')\n",
    "    else:\n",
    "        print('false')\n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4\n",
      "0\n",
      "true\n",
      "1\n",
      "false\n",
      "2\n",
      "true\n",
      "3\n",
      "false\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "for i in range(n):\n",
    "    x = int(input())\n",
    "    if x%2==0:\n",
    "        print(\"true\")\n",
    "    else:\n",
    "        print(\"false\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 136,
   "metadata": {},
   "outputs": [],
   "source": [
    "from ipywidgets import interact,interactive,fixed\n",
    "import ipywidgets as widgets\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 140,
   "metadata": {},
   "outputs": [],
   "source": [
    "def func(x):\n",
    "    return x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 144,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a9db0959d91040b7ac08aa4cbf1e6328",
       "version_major": 2,
       "version_minor": 0
      },
      "text/html": [
       "<p>Failed to display Jupyter Widget of type <code>interactive</code>.</p>\n",
       "<p>\n",
       "  If you're reading this message in the Jupyter Notebook or JupyterLab Notebook, it may mean\n",
       "  that the widgets JavaScript is still loading. If this message persists, it\n",
       "  likely means that the widgets JavaScript library is either not installed or\n",
       "  not enabled. See the <a href=\"https://ipywidgets.readthedocs.io/en/stable/user_install.html\">Jupyter\n",
       "  Widgets Documentation</a> for setup instructions.\n",
       "</p>\n",
       "<p>\n",
       "  If you're reading this message in another frontend (for example, a static\n",
       "  rendering on GitHub or <a href=\"https://nbviewer.jupyter.org/\">NBViewer</a>),\n",
       "  it may mean that your frontend doesn't currently support widgets.\n",
       "</p>\n"
      ],
      "text/plain": [
       "interactive(children=(Text(value='hlelo', description='x'), Output()), _dom_classes=('widget-interact',))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "<function __main__.func>"
      ]
     },
     "execution_count": 144,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "interact(func,x=\"hlelo\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "1 2 3 4 5 6 7 8 9 10 \n",
      "\n",
      "         1\n",
      "        222\n",
      "       33333\n",
      "      4444444\n",
      "     555555555\n",
      "    66666666666\n",
      "   7777777777777\n",
      "  888888888888888\n",
      " 99999999999999999\n",
      "10101010101010101010101010101010101010\n",
      "10101010101010101010101010101010101010\n",
      " 99999999999999999\n",
      "  888888888888888\n",
      "   7777777777777\n",
      "    66666666666\n",
      "     555555555\n",
      "      4444444\n",
      "       33333\n",
      "        222\n",
      "         1\n"
     ]
    }
   ],
   "source": [
    "n = int(input())\n",
    "for i in range(1,n+1):\n",
    "    print(\"{}\".format(i),end=' ')\n",
    "print('\\n')\n",
    "p=n/2\n",
    "for i in range(1,n+1):\n",
    "    p=n-i\n",
    "    print(p*\" \"+(2*i-1)*\"{}\".format(i))\n",
    "for i in range(n,0,-1):\n",
    "    p=n-i\n",
    "    print(p*' '+(2*i-1)*'{}'.format(i))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "os.chdir('D:\\Machine Learning\\Machine Learning A-Z Template Folder\\Part 1 - Data Preprocessing')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'D:\\\\Machine Learning\\\\Machine Learning A-Z Template Folder\\\\Part 1 - Data Preprocessing'"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset = pd.read_csv('Data.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [],
   "source": [
    "x=dataset.iloc[:,:-1].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([['France', 44.0, 72000.0],\n",
       "       ['Spain', 27.0, 48000.0],\n",
       "       ['Germany', 30.0, 54000.0],\n",
       "       ['Spain', 38.0, 61000.0],\n",
       "       ['Germany', 40.0, nan],\n",
       "       ['France', 35.0, 58000.0],\n",
       "       ['Spain', nan, 52000.0],\n",
       "       ['France', 48.0, 79000.0],\n",
       "       ['Germany', 50.0, 83000.0],\n",
       "       ['France', 37.0, 67000.0]], dtype=object)"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import Imputer\n",
    "imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)\n",
    "imputer = imputer.fit(x[:, 1:3])\n",
    "x[:, 1:3] = imputer.transform(x[:, 1:3])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[0, 44.0, 72000.0],\n",
       "       [2, 27.0, 48000.0],\n",
       "       [1, 30.0, 54000.0],\n",
       "       [2, 38.0, 61000.0],\n",
       "       [1, 40.0, 63777.77777777778],\n",
       "       [0, 35.0, 58000.0],\n",
       "       [2, 38.77777777777778, 52000.0],\n",
       "       [0, 48.0, 79000.0],\n",
       "       [1, 50.0, 83000.0],\n",
       "       [0, 37.0, 67000.0]], dtype=object)"
      ]
     },
     "execution_count": 57,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import LabelEncoder, OneHotEncoder\n",
    "labelencoder_x = LabelEncoder()\n",
    "x[:, 0] = labelencoder_x.fit_transform(x[:, 0])\n",
    "onehotencoder = OneHotEncoder(categorical_features = [0])\n",
    "x = onehotencoder.fit_transform(x).toarray()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1.00000000e+00, 0.00000000e+00, 0.00000000e+00, 4.40000000e+01,\n",
       "        7.20000000e+04],\n",
       "       [0.00000000e+00, 0.00000000e+00, 1.00000000e+00, 2.70000000e+01,\n",
       "        4.80000000e+04],\n",
       "       [0.00000000e+00, 1.00000000e+00, 0.00000000e+00, 3.00000000e+01,\n",
       "        5.40000000e+04],\n",
       "       [0.00000000e+00, 0.00000000e+00, 1.00000000e+00, 3.80000000e+01,\n",
       "        6.10000000e+04],\n",
       "       [0.00000000e+00, 1.00000000e+00, 0.00000000e+00, 4.00000000e+01,\n",
       "        6.37777778e+04],\n",
       "       [1.00000000e+00, 0.00000000e+00, 0.00000000e+00, 3.50000000e+01,\n",
       "        5.80000000e+04],\n",
       "       [0.00000000e+00, 0.00000000e+00, 1.00000000e+00, 3.87777778e+01,\n",
       "        5.20000000e+04],\n",
       "       [1.00000000e+00, 0.00000000e+00, 0.00000000e+00, 4.80000000e+01,\n",
       "        7.90000000e+04],\n",
       "       [0.00000000e+00, 1.00000000e+00, 0.00000000e+00, 5.00000000e+01,\n",
       "        8.30000000e+04],\n",
       "       [1.00000000e+00, 0.00000000e+00, 0.00000000e+00, 3.70000000e+01,\n",
       "        6.70000000e+04]])"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5 3\n",
      "1 2 3 4 5\n",
      "1 2\n",
      "2 3\n",
      "3 4\n",
      "1\n",
      "2\n",
      "3\n"
     ]
    }
   ],
   "source": [
    "n,m=map(int,input().split())\n",
    "x=input().split()\n",
    "lst=[]\n",
    "for i in range(m):\n",
    "    lst.append(map(int, input().split()))\n",
    "for x,y in lst:\n",
    "    print((x+y)//2)\n",
    "\n",
    "    \n",
    "\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = [int(i) for i in input().split()]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20/25\n",
      "4 / 5\n"
     ]
    }
   ],
   "source": [
    "from fractions import Fraction\n",
    "f = input().replace(\" / \", \"/\")\n",
    "try:\n",
    "    red = str(Fraction(f))\n",
    "    print(red.replace(\"/\", \" / \"))\n",
    "except:\n",
    "    print(\"INVALID\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "8/5\n"
     ]
    }
   ],
   "source": [
    "from fractions import Fraction\n",
    "f = input().replace(\" / \", \"/\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1/2\n"
     ]
    }
   ],
   "source": [
    "print((Fraction(f)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    " import smtplib\n",
    "    text = \"You are being watched\"\n",
    "    ml = smtplib.SMTP ('smtp.gmail.com',587)\n",
    "    ml.ehlo()\n",
    "    ml.starttls()\n",
    "    ml.login('boyapatisaiteja@gmail.com','04vamsi@1998')\n",
    "    ml.sendmail('ravi@gmail.com','saitejaboyapati.com',text)\n",
    "    ml.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "for i in range(2):\n",
    "    import smtplib\n",
    "    text = \"You are being watched\"\n",
    "    ml = smtplib.SMTP ('smtp.gmail.com',587)\n",
    "    ml.ehlo()\n",
    "    ml.starttls()\n",
    "    ml.login('boyapatisaiteja@gmail.com','04vamsi@1998')\n",
    "    ml.sendmail('ravi@gmail.com','saitejaboyapati.com',text)\n",
    "    ml.close()\n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
