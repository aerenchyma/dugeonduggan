#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
#import urllib
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)), extensions=['jinja2.ext.autoescape'])

def minEditDist(seq1, seq2):
    """Calculate the Damerau-Levenshtein distance between sequences.

    This distance is the number of additions, deletions, substitutions,
    and transpositions needed to transform the first sequence into the
    second. Although generally used with strings, any sequences of
    comparable objects will work.

    Transpositions are exchanges of *consecutive* characters; all other
    operations are self-explanatory.

    This implementation is O(N*M) time and O(M) space, for N and M the
    lengths of the two sequences.

    >>> dameraulevenshtein('ba', 'abc')
    2
    >>> dameraulevenshtein('fee', 'deed')
    2

    It works with arbitrary sequences too:
    >>> dameraulevenshtein('abcd', ['b', 'a', 'c', 'd', 'e'])
    2
    """
    # codesnippet:D0DE4716-B6E6-4161-9219-2903BF8F547F
    # Conceptually, this is based on a len(seq1) + 1 * len(seq2) + 1 matrix.
    # However, only the current and two previous rows are needed at once,
    # so we only store those.
    oneago = None
    thisrow = range(1, len(seq2) + 1) + [0]
    for x in xrange(len(seq1)):
        # Python lists wrap around for negative indices, so put the
        # leftmost column at the *end* of the list. This matches with
        # the zero-indexed strings and saves extra calculation.
        twoago, oneago, thisrow = oneago, thisrow, [0] * len(seq2) + [x + 1]
        for y in xrange(len(seq2)):
            delcost = oneago[y] + 1
            addcost = thisrow[y - 1] + 1
            subcost = oneago[y - 1] + (seq1[x] != seq2[y])
            thisrow[y] = min(delcost, addcost, subcost)
            # This block deals with transpositions
            if (x > 0 and y > 0 and seq1[x] == seq2[y - 1]
                and seq1[x-1] == seq2[y] and seq1[x] != seq2[y]):
                thisrow[y] = min(thisrow[y], twoago[y - 2] + 1)
    return thisrow[len(seq2) - 1]

def decide_vote(cand):
  if not cand:
    return "..."
  if minEditDist(cand, "Duggan") < minEditDist(cand, "Dugeon"):
    return "closer to Duggan"
  elif minEditDist(cand, "Dugeon") < minEditDist(cand, "Duggan"):
    return "closer to Dugeon"
  elif minEditDist(cand, "Dugeon") == minEditDist(cand, "Duggan"):
    return "too close to call"
  else:
    return ""

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	template_values = {}
    	candidate = self.request.get('candidate', "")

    	template_values["candidate"] = candidate
    	template_values["result"] = decide_vote(candidate)

    	template = JINJA_ENVIRONMENT.get_template('templates/result.html')

        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
