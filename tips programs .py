{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8b6b3883",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pod\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1e158a7d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>total_bill</th>\n",
       "      <th>tip</th>\n",
       "      <th>sex</th>\n",
       "      <th>smoker</th>\n",
       "      <th>day</th>\n",
       "      <th>time</th>\n",
       "      <th>size</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>16.99</td>\n",
       "      <td>1.01</td>\n",
       "      <td>Female</td>\n",
       "      <td>No</td>\n",
       "      <td>Sun</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>10.34</td>\n",
       "      <td>1.66</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>Sun</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>21.01</td>\n",
       "      <td>3.50</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>Sun</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>23.68</td>\n",
       "      <td>3.31</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>Sun</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>24.59</td>\n",
       "      <td>3.61</td>\n",
       "      <td>Female</td>\n",
       "      <td>No</td>\n",
       "      <td>Sun</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>239</th>\n",
       "      <td>29.03</td>\n",
       "      <td>5.92</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>Sat</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>240</th>\n",
       "      <td>27.18</td>\n",
       "      <td>2.00</td>\n",
       "      <td>Female</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Sat</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>241</th>\n",
       "      <td>22.67</td>\n",
       "      <td>2.00</td>\n",
       "      <td>Male</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Sat</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>242</th>\n",
       "      <td>17.82</td>\n",
       "      <td>1.75</td>\n",
       "      <td>Male</td>\n",
       "      <td>No</td>\n",
       "      <td>Sat</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>243</th>\n",
       "      <td>18.78</td>\n",
       "      <td>3.00</td>\n",
       "      <td>Female</td>\n",
       "      <td>No</td>\n",
       "      <td>Thur</td>\n",
       "      <td>Dinner</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>244 rows × 7 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     total_bill   tip     sex smoker   day    time  size\n",
       "0         16.99  1.01  Female     No   Sun  Dinner     2\n",
       "1         10.34  1.66    Male     No   Sun  Dinner     3\n",
       "2         21.01  3.50    Male     No   Sun  Dinner     3\n",
       "3         23.68  3.31    Male     No   Sun  Dinner     2\n",
       "4         24.59  3.61  Female     No   Sun  Dinner     4\n",
       "..          ...   ...     ...    ...   ...     ...   ...\n",
       "239       29.03  5.92    Male     No   Sat  Dinner     3\n",
       "240       27.18  2.00  Female    Yes   Sat  Dinner     2\n",
       "241       22.67  2.00    Male    Yes   Sat  Dinner     2\n",
       "242       17.82  1.75    Male     No   Sat  Dinner     2\n",
       "243       18.78  3.00  Female     No  Thur  Dinner     2\n",
       "\n",
       "[244 rows x 7 columns]"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tips=sns.load_dataset(\"tips\")\n",
    "tips"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "95da98ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Thur    0\n",
       "Fri     0\n",
       "Sat     0\n",
       "Sun     0\n",
       "Name: day, dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#39Q\n",
    "tips[tips[\"sex\"]==\"female\"][\"day\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "98a61cba",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Series([], Name: day, dtype: category\n",
       "Categories (4, object): ['Thur', 'Fri', 'Sat', 'Sun'])"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "tips[tips[\"sex\"]==\"female\"][\"day\"].mode()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "819b4301",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    Thur\n",
       "Name: day, dtype: category\n",
       "Categories (4, object): ['Thur', 'Fri', 'Sat', 'Sun']"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#38Q\n",
    "tips[tips[\"time\"]==\"Lunch\"][\"day\"].mode()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "66feacc8",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\SRAM30\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\seaborn\\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='day', ylabel='count'>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAX4AAAEGCAYAAABiq/5QAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAQJ0lEQVR4nO3df5BdZX3H8ffHBCoqFDDbGI3tMm0Gi79QV6q1thVq/S2MpQwO2oBM4x/V6tjW0jqj1rYzdkprGfw1KQihowWKUqK2ViZKrR1L3ShVflSlmChIyIJkBGuxod/+cU9kSXY3N0vOvbs879fMzj3nuefc850zu5/77HPPeW6qCklSOx4x7gIkSaNl8EtSYwx+SWqMwS9JjTH4JakxK8ddwDBWrVpVk5OT4y5DkpaVrVu33llVE3u3L4vgn5ycZHp6etxlSNKykmT7XO0O9UhSYwx+SWqMwS9JjTH4JakxBr8kNcbgl6TGGPyS1BiDX5IaY/BLUmN6vXM3yZHABcBTgAJeB3wNuAyYBLYBp1XV3Q/lOM/6vUseyu4PK1v//DfGXYKkJa7vHv95wKeq6knA04GbgHOALVW1DtjSrUuSRqS34E/y48AvAhcCVNUPq2oXcDKwqdtsE3BKXzVIkvbVZ4//GGAGuCjJl5NckOTRwOqqur3bZgeweq6dk2xIMp1kemZmpscyJaktfQb/SuCZwAeq6hnA99lrWKcG3/Q+57e9V9XGqpqqqqmJiX1mFZUkLVKfwX8rcGtVXdutX8HgjeCOJGsAusedPdYgSdpLb8FfVTuAbyc5tms6CbgR2Ays79rWA1f1VYMkaV99fxHLG4EPJzkUuAU4i8GbzeVJzga2A6f1XIMkaZZeg7+qrgOm5njqpD6PK0man3fuSlJjDH5JaozBL0mNMfglqTEGvyQ1xuCXpMYY/JLUGINfkhpj8EtSYwx+SWqMwS9JjTH4JakxBr8kNcbgl6TGGPyS1BiDX5IaY/BLUmMMfklqjMEvSY0x+CWpMQa/JDXG4Jekxhj8ktQYg1+SGmPwS1JjVvb54km2AfcA9wO7q2oqydHAZcAksA04raru7rMOSdIDRtHjf0FVHV9VU936OcCWqloHbOnWJUkjMo6hnpOBTd3yJuCUMdQgSc3qO/gL+HSSrUk2dG2rq+r2bnkHsHquHZNsSDKdZHpmZqbnMiWpHb2O8QO/UFW3JfkJ4Ook/zn7yaqqJDXXjlW1EdgIMDU1Nec2kqQD12uPv6pu6x53AlcCJwB3JFkD0D3u7LMGSdKD9Rb8SR6d5PA9y8CvAtcDm4H13Wbrgav6qkGStK8+h3pWA1cm2XOcj1TVp5J8Ebg8ydnAduC0HmuQJO2lt+CvqluAp8/RfhdwUl/HlSQtzDt3JakxBr8kNcbgl6TGGPyS1BiDX5IaY/BLUmMMfklqjMEvSY0x+CWpMQa/JDXG4Jekxhj8ktQYg1+SGmPwS1JjDH5JaozBL0mNMfglqTEGvyQ1xuCXpMYY/JLUGINfkhpj8EtSYwx+SWqMwS9JjTH4JakxvQd/khVJvpzkE936MUmuTXJzksuSHNp3DZKkB4yix/8m4KZZ638GvKeqfga4Gzh7BDVIkjq9Bn+StcDLgAu69QAnAld0m2wCTumzBknSg/Xd4/8r4K3A/3XrjwV2VdXubv1W4Alz7ZhkQ5LpJNMzMzM9lylJ7egt+JO8HNhZVVsXs39VbayqqaqampiYOMjVSVK7Vvb42s8DXpnkpcAjgSOA84Ajk6zsev1rgdt6rEGStJfeevxV9QdVtbaqJoHTgc9U1RnAZ4FTu83WA1f1VYMkaV/juI7/94G3JLmZwZj/hWOoQZKa1edQz49U1TXANd3yLcAJoziuJGlf3rkrSY0x+CWpMQa/JDXG4Jekxhj8ktQYg1+SGmPwS1JjDH5JaozBL0mNMfglqTFDBX+SLcO0SZKWvgXn6knySOBRwKokRwHpnjqCeb5ARZK0tO1vkrbXA28GHg9s5YHg/x7w3v7KkiT1ZcHgr6rzgPOSvLGqzh9RTZKkHg01LXNVnZ/k54HJ2ftU1SU91SVJ6slQwZ/kb4CfBq4D7u+aCzD4JWmZGfaLWKaA46qq+ixGktS/Ya/jvx54XJ+FSJJGY9ge/yrgxiT/Dty3p7GqXtlLVZKk3gwb/O/sswhJ0ugMe1XPP/ddiCRpNIa9quceBlfxABwKHAJ8v6qO6KswSVI/hu3xH75nOUmAk4Hn9FWUJKk/Bzw7Zw38PfCig1+OJKlvww71vGrW6iMYXNf/P71UJEnq1bBX9bxi1vJuYBuD4Z55dTN7fg74se44V1TVO5IcA1wKPJbBxG+vraofHmDdkqRFGnaM/6xFvPZ9wIlVdW+SQ4DPJ/lH4C3Ae6rq0iQfBM4GPrCI15ckLcKwX8SyNsmVSXZ2Px9NsnahfbrPAu7tVg/pfgo4Ebiia98EnLK40iVJizHsh7sXAZsZzMv/eODjXduCkqxIch2wE7ga+C9gV1Xt7ja5lXm+0CXJhiTTSaZnZmaGLFOStD/DBv9EVV1UVbu7n4uBif3tVFX3V9XxwFrgBOBJwxZWVRuraqqqpiYm9nsoSdKQhg3+u5K8puvBr0jyGuCuYQ9SVbuAzwLPBY5MsuezhbXAbQdSsCTpoRk2+F8HnAbsAG4HTgXOXGiHJBNJjuyWDwNeCNzE4A3g1G6z9cBVB1q0JGnxhr2c813A+qq6GyDJ0cC5DN4Q5rMG2JRkBYM3mMur6hNJbgQuTfInwJeBCxddvSTpgA0b/E/bE/oAVfXdJM9YaIeq+gqwzzZVdQuD8X5J0hgMO9TziCRH7VnpevzDvmlIkpaQYcP7L4AvJPm7bv3XgT/tpyRJUp+GvXP3kiTTDG6+AnhVVd3YX1mSpL4MPVzTBb1hL0nL3AFPyyxJWt4MfklqjMEvSY0x+CWpMQa/JDXG4Jekxhj8ktQYg1+SGmPwS1JjDH5JaozBL0mNMfglqTEGvyQ1xuCXpMYY/JLUGINfkhpj8EtSYwx+SWqMwS9JjTH4JakxBr8kNaa34E/yxCSfTXJjkhuSvKlrPzrJ1Um+0T0e1VcNkqR99dnj3w38TlUdBzwH+K0kxwHnAFuqah2wpVuXJI1Ib8FfVbdX1Ze65XuAm4AnACcDm7rNNgGn9FWDJGlfIxnjTzIJPAO4FlhdVbd3T+0AVs+zz4Yk00mmZ2ZmRlGmJDWh9+BP8hjgo8Cbq+p7s5+rqgJqrv2qamNVTVXV1MTERN9lSlIzeg3+JIcwCP0PV9XHuuY7kqzpnl8D7OyzBknSg/V5VU+AC4GbquovZz21GVjfLa8HruqrBknSvlb2+NrPA14LfDXJdV3bHwLvBi5PcjawHTitxxokSXvpLfir6vNA5nn6pL6OK0lamHfuSlJjDH5JaozBL0mNMfglqTEGvyQ1xuCXpMYY/JLUGINfkhpj8EtSYwx+SWqMwS9JjTH4JakxBr8kNcbgl6TGGPyS1BiDX5IaY/BLUmMMfklqjMEvSY0x+CWpMQa/JDXG4Jekxhj8ktQYg1+SGmPwS1Jjegv+JB9KsjPJ9bPajk5ydZJvdI9H9XV8SdLc+uzxXwy8eK+2c4AtVbUO2NKtS5JGqLfgr6rPAd/dq/lkYFO3vAk4pa/jS5LmNuox/tVVdXu3vANYPd+GSTYkmU4yPTMzM5rqJKkBY/twt6oKqAWe31hVU1U1NTExMcLKJOnhbdTBf0eSNQDd484RH1+Smjfq4N8MrO+W1wNXjfj4ktS8Pi/n/FvgC8CxSW5NcjbwbuCFSb4B/Eq3LkkaoZV9vXBVvXqep07q65iSpP3zzl1JaozBL0mNMfglqTEGvyQ1prcPd7V8fetdTx13CUvGT779q+MuQTro7PFLUmMMfklqjMEvSY0x+CWpMQa/JDXG4Jekxhj8ktQYg1+SGmPwS1JjDH5JaozBL0mNMfglqTEGvyQ1xuCXpMYY/JLUGINfkhpj8EtSYwx+SWqMwS9JjTH4JakxYwn+JC9O8rUkNyc5Zxw1SFKrRh78SVYA7wNeAhwHvDrJcaOuQ5JaNY4e/wnAzVV1S1X9ELgUOHkMdUhSk1aO4ZhPAL49a/1W4Of23ijJBmBDt3pvkq+NoLaHahVw5zgLyLnrx3n4g2ns5xKAd2TcFRwsS+N8Pnwsl/P5U3M1jiP4h1JVG4GN467jQCSZrqqpcdfxcOC5PLg8nwfXcj+f4xjquQ144qz1tV2bJGkExhH8XwTWJTkmyaHA6cDmMdQhSU0a+VBPVe1O8gbgn4AVwIeq6oZR19GTZTU0tcR5Lg8uz+fBtazPZ6pq3DVIkkbIO3clqTEGvyQ1xuBfQJLHJrmu+9mR5LZueVeSG8dd38NFkvtnnefrkkzOsc0/JDly9NUtL0neluSGJF/pzuU+98jM2vbMJI8fZX3LxYGcx+VoyV7HvxRU1V3A8QBJ3gncW1XndsH0icW+bpKVVbX7YNT4MPGDqjp+rieShMFnUS8dbUnLT5LnAi8HnllV9yVZBRy6wC5nAtcD3xlBecvGIs7jsmOPf/FWJPnrrlfw6SSHASS5JslUt7wqybZu+cwkm5N8BtgyvrKXviST3SR+lzAIpicm2db9AWp+a4A7q+o+gKq6s6q+k+TtSb6Y5PokGzNwKjAFfLjr0R421sqXlvnO449+B5NMJbmmW35nkg91f/u3JPnt8ZU+HIN/8dYB76uqJwO7gF8bYp9nAqdW1S/1WdgydNisYZ4ru7Z1wPur6slVtX2cxS0jn2bwJvn1JO9Psuf37L1V9eyqegpwGPDyqroCmAbOqKrjq+oH4yp6CZrvPC7kScCLGMxF9o4kh/Ra4UPkUM/ifbOqruuWtwKTQ+xzdVV9t7eKlq8HDfV0Q2nbq+rfxlbRMlRV9yZ5FvB84AXAZd205/ckeSvwKOBo4Abg4+OrdGlb4Dwu5JPdfwj3JdkJrGYwD9mSZPAv3n2zlu9n0JMC2M0D/0k9cq99vt93UQ8jnqtFqKr7gWuAa5J8FXg98DRgqqq+3X1WtffvpfYyx3lcz8J/23vnwZLOVod6Dr5twLO65VPHWIcak+TYJOtmNR0P7JnV9s4kj+HBv5P3AIePqLxlY57zuJ0H/20PM7S7ZC3pd6Vl6lzg8m5a6U+Ouxg15THA+d1lr7uBmxlMbb6LwYfkOxjMlbXHxcAHk/wAeK7j/D8y33n8WeDCJH/M4L+BZcspGySpMQ71SFJjDH5JaozBL0mNMfglqTEGvyQ1xuCXDkA3L8vvjrsO6aEw+CWpMQa/tB/d3OxfT/J54Niu7Te7GS//I8lHkzwqyeFJvrlngq4kR8xel5YKg19aQDdZ1+kMbtt/KfDs7qmPdTNePh24CTi7qu5hcEfny7ptTu+2+9+RFi3th8EvLez5wJVV9d9V9T1gc9f+lCT/0k3gdQbw5K79AuCsbvks4KKRVisNweCXFudi4A1V9VTgj+hma6yqfwUmk/wysKKqrh9XgdJ8DH5pYZ8DTklyWJLDgVd07YcDt3fj92fstc8lwEewt68lyknapP1I8jYG87HvBL4FfInB9wW8FZgBrgUOr6ozu+0fB3wTWFNVu8ZQsrQgg186yLrvsz25ql477lqkuTgfv3QQJTkfeAmDK4CkJckevyQ1xg93JakxBr8kNcbgl6TGGPyS1BiDX5Ia8/+urAB6u60QYgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot(\"day\",data=tips[tips[\"time\"]==\"Lunch\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "c49528b9",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\SRAM30\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\seaborn\\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='day', ylabel='count'>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.countplot('day',data=tips,hue=\"time\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "f8379bf7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2    53\n",
       "3    18\n",
       "4    13\n",
       "1     2\n",
       "5     1\n",
       "Name: size, dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#37Q\n",
    "tips[tips[\"day\"]==\"Sat\"][\"size\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "03f63408",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sun     18\n",
       "Sat     13\n",
       "Thur     5\n",
       "Fri      1\n",
       "Name: day, dtype: int64"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#36Q\n",
    "tips[tips[\"size\"]==4][\"day\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "6ac51809",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    Sun\n",
       "Name: day, dtype: category\n",
       "Categories (4, object): ['Thur', 'Fri', 'Sat', 'Sun']"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tips[tips[\"size\"]==4][\"day\"].mode()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "74b1ada6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Dinner    4\n",
       "Lunch     1\n",
       "Name: time, dtype: int64"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#35Q\n",
    "tips[tips[\"size\"]==5][\"time\"].value_counts()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "3c48f9ef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    Dinner\n",
       "Name: time, dtype: category\n",
       "Categories (2, object): ['Lunch', 'Dinner']"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tips[tips[\"size\"]==5][\"time\"].mode()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "fa52316f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>total_bill</th>\n",
       "      <th>tip</th>\n",
       "      <th>sex</th>\n",
       "      <th>smoker</th>\n",
       "      <th>day</th>\n",
       "      <th>time</th>\n",
       "      <th>size</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>121</th>\n",
       "      <td>13.42</td>\n",
       "      <td>1.68</td>\n",
       "      <td>Female</td>\n",
       "      <td>No</td>\n",
       "      <td>Thur</td>\n",
       "      <td>Lunch</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>221</th>\n",
       "      <td>13.42</td>\n",
       "      <td>3.48</td>\n",
       "      <td>Female</td>\n",
       "      <td>Yes</td>\n",
       "      <td>Fri</td>\n",
       "      <td>Lunch</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     total_bill   tip     sex smoker   day   time  size\n",
       "121       13.42  1.68  Female     No  Thur  Lunch     2\n",
       "221       13.42  3.48  Female    Yes   Fri  Lunch     2"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#34Q\n",
    "tips1 = tips[((tips['total_bill']==13.42) & (tips['sex']==\"Female\"))]\n",
    "tips1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "1a19b8b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "#33Q"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "ee08ab2e",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\SRAM30\\AppData\\Local\\Temp\\ipykernel_7492\\55100422.py:2: FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.\n",
      "  tips.groupby(\"sex\")[\"total_bill\",\"tip\"].mean()\n"
     ]
    },
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>total_bill</th>\n",
       "      <th>tip</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>sex</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Male</th>\n",
       "      <td>20.744076</td>\n",
       "      <td>3.089618</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Female</th>\n",
       "      <td>18.056897</td>\n",
       "      <td>2.833448</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        total_bill       tip\n",
       "sex                         \n",
       "Male     20.744076  3.089618\n",
       "Female   18.056897  2.833448"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#32Q\n",
    "tips.groupby(\"sex\")[\"total_bill\",\"tip\"].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "2fe70001",
   "metadata": {},
   "outputs": [],
   "source": [
    "#30Q\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "c2c94a30",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "day\n",
       "Thur    17.682742\n",
       "Fri     17.151579\n",
       "Sat     20.441379\n",
       "Sun     21.410000\n",
       "Name: total_bill, dtype: float64"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#29Q\n",
    "tips.groupby(\"day\")[\"total_bill\"].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "a0c41a8f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x23e4971f1c0>"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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YKGUch6A/w3j+YmIiIiIiIiIiIgojMJWYJZSbgIw+J6nPwfgv6WU41Ov6Q3X+YmIiIiIiIiIiIgovCLdg3kWgHVCiO1CiI1CiOUne6EQ4tNCiGohRHVfX18EI6pVUFgEIUTIHwWFRar/aEQU5RJ13CUiUiFRx1xe6xKRKok67hIRRYKQUobv4EIUA3hOSlk19fsaAK8D+BKA5QAeAVAqPyDEsmXLZHV1ddhyRhMhBO5+6UjIj3vXxZUI5781EUUlMdMvTKRxl4gohGY07ibSmMtrXSIKMY67RESRdcJxN9IzmNsBPCEn7QAQBJAe4QxEREREREREREREFAKRLjA/BeA8ABBCzAJgANAf4QxEREREREREREREFAK6cB1YCPEQgHMBpAsh2gF8H8C9AO6dapXhA3D7B7XHICIiIiIiIiIiIqLoFLYCs5TylpN86rZwnZOIiIiIiIiIiIiIIifSLTKIiIiIiIiIiIiIKE6wwExEREREREREREREM8ICMxERERERERERERHNCAvMRERERERERERERDQjLDATERERERERERER0YywwExEREREREREREREM8ICMxERERERERERERHNCAvMRERERERERERERDQjLDATERERERERERER0YywwExEREREREREREREM8ICMxERERERERERERHNCAvMRERERERERERERDQjOtUBiIiIiIiIzojQQAgR8sNqdXoE/BMhP25+QSHaWltCflwiIiIiFVhgJiIiIiKi2CaDuPulIyE/7F0XV4btuERERETxgi0yiIiIiIiIiIiIiGhGWGAmIiIiIiIiIiIiohlhiwwiIiIiIiIAQy4fOkc8GHZPQAggefEV6HF6kWk1hqXHMxEREVE8YIGZiIiIiIgSlpQSTf0u7GgeRI9zHAAgBAAJpF38OTy8sw0Oix6LCuyoyk2BRsNCMxEREdHxWGAmIiIiIqKE5Pb58XJtD5oH3LCb9VhXkY6S9CSkmPUQAL55/Trc8ZvnUdPhxOtH+nCgYwQXzc1CptWkOjoRERFR1GCBmYiIiIiIEk7vqBfP7uuCZyKAsyvSsSDfDu17ZicHRvswLzcFc3NsONrnwht1vXi0uh3nz87E3BybouRERERE0YUFZiIiIiIiSihdIx48tbcTRp0GNy7L/8AZyUIIlGcmI9duwoaabrxc2wOvL4AlRY4IJSYi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\n",
      "text/plain": [
       "<Figure size 1440x360 with 4 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.displot(data=tips,x=\"total_bill\",col=\"day\",kde=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b0004c7",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
