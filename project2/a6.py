# a6.py
# Lini Tan (lt398)
# Nov.15
"""Classes to perform KMeans Clustering"""

import math
import random
import numpy

# HELPER FUNCTIONS FOR ASSERTS GO HERE
def is_point(thelist):
    """Return: True if thelist is a list of int or float"""
    if (type(thelist) != list):
        return False
    
    # All float
    okay = True
    for x in thelist:
        if (not type(x) in [int,float]):
            okay = False
    
    return okay


def is_point_list(thelist):
    """Return: True if thelist is a list and every element in the list is a point
    and every element in the list has the same length."""
    if thelist is None:
        return True
    
    for x in range(len(thelist)):
        if is_point(thelist[x]) == True and len(thelist[x]) == len(thelist[x-1]):
            return True
        else:
            return False


def is_k_list(thelist,ds):
    """Return: True if thelist is None, or a list of k valid indices into ds.
    """
    if thelist is None:
        return True
    
    if not (type(thelist) == list) and 0 < len(thelist) <= ds.getSize():
        return False
    
    okay = True
    for x in thelist:
        if not (type(x) == int and 0 <= x < ds.getSize()):
            okay = False
    return okay

        
# CLASSES
class Dataset(object):
    """Instance is a dataset for k-means clustering.
    
    The data is stored as a list of list of numbers
    (ints or floats).  Each component list is a data point.
    
    Instance Attributes:
        _dimension: the point dimension for this dataset
            [int > 0. Value never changes after initialization]
        
        _contents: the dataset contents
            [a 2D list of numbers (float or int), possibly empty]:
    
    ADDITIONAL INVARIANT:
        The number of columns in _contents is equal to _dimension.  
        That is, for every item _contents[i] in the list _contents, 
        len(_contents[i]) == dimension.
    
    None of the attributes should be accessed directly outside of the class
    Dataset (e.g. in the methods of class Cluster or KMeans). Instead, this class 
    has getter and setter style methods (with the appropriate preconditions) for 
    modifying these values.
    """
    
    def __init__(self, dim, contents=None):
        """Initializer: Creates a dataset for the given point dimension.
        
        Note that contents (which is the initial value for attribute _contents)
        is optional. When assigning contents to the attribute _contents the initializer
        COPIES the  list contents. If contents is None, the initializer assigns 
        _contents an empty list.
        
        Parameter dim: the initial value for attribute _dimension.  
        Precondition: dim is an int > 0.
        
        Parameter contents: the initial value for attribute _contents (optional). 
        Precondition: contents is either None or is a 2D list of numbers (int or float). 
        If contents is not None, then contents if not empty and the number of columns of 
        contents is equal to dim.
        """
        # IMPLEMENT ME
        assert type(dim) == int and dim > 0
        assert is_point_list(contents)
        self._dimension = dim
        if contents is None:
            self._contents = []
        else :
            self._contents = []
            for x in contents:
                self._contents.append(x[:])
  
    
    def getDimension(self):
        """Returns: The point dimension of this data set.
        """
        # IMPLEMENT ME
        return self._dimension
  
    
    def getSize(self):
        """Returns: the number of elements in this data set.
        """
        # IMPLEMENT ME
        return len(self._contents)
 
   
    def getContents(self):
        """Returns: The contents of this data set as a list.
        
        This method returns the attribute _contents directly.  Any changes made to this 
        list will modify the data set.  If you want to access the data set, but want to 
        protect yourself from modifying the data, use getPoint() instead.
        """
        # IMPLEMENT ME
        return self._contents
 
   
    def getPoint(self, i):
        """Returns: A COPY of the point at index i in this data set.
        
        Often, we want to access a point in the data set, but we want a copy
        to make sure that we do not accidentally modify the data set.  That
        is the purpose of this method.  
        
        If you actually want to modify the data set, use the method getContents().
        That returns the list storing the data set, and any changes to that
        list will alter the data set.
        
        Parameter i: the index position of the point
        Precondition: i is an int that refers to a valid position in 0..getSize()-1
        """
        assert type(i)==int and 0 <= i <= self.getSize()-1
        copypoint = self._contents[i][:]
        return copypoint
  
    
    def addPoint(self,point):
        """Adds a COPY of point at the end of _contents.
        
        This method does not add the point directly. It adds a copy of the point.
        
        Parameter point: the point to add
        Precondition: point is a list of numbers (int or float), len(point) = _dimension.
        """
        assert is_point(point)
        newpoint = point[:]
        self._contents.append(newpoint)
   
        
    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """Returns: String representation of the centroid of this cluster."""
        return str(self._contents)
    
    
    def __repr__(self):
        """Returns: Unambiguous representation of this cluster. """
        return str(self.__class__) + str(self)


class Cluster(object):
    """An instance is a cluster, a subset of the points in a dataset.
    
    A cluster is represented as a list of integers that give the indices
    in the dataset of the points contained in the cluster.  For instance,
    a cluster consisting of the points with indices 0, 4, and 5 in the
    dataset's data array would be represented by the index list [0,4,5].
    
    A cluster instance also contains a centroid that is used as part of
    the k-means algorithm.  This centroid is an n-D point (where n is
    the dimension of the dataset), represented as a list of n numbers,
    not as an index into the dataset.  (This is because the centroid
    is generally not a point in the dataset, but rather is usually in between
    the data points.)
    
    Instance Attributes:
        _dataset: the dataset this cluster is a subset of  [Dataset]
        
        _indices: the indices of this cluster's points in the dataset  [list of int]
        
        _centroid: the centroid of this cluster  [list of numbers]
    
    ADDITIONAL INVARIANTS:
        len(_centroid) == _dataset.getDimension()
        0 <= _indices[i] < _dataset.getSize(), for all 0 <= i < len(_indices)
    """
   
    
    # Part A
    def __init__(self, ds, centroid):
        """Initializer: Creates a new empty cluster with the given centroid.
        
        Remember that a centroid is a point and hence a list.  The initializer COPIES
        the centroid; it does not use the original list.
        
        IMPORTANT: READ THE PRECONDITION OF ds VERY CAREFULLY
        
        Parameter ds: the Dataset for this cluster
        Precondition: ds is a instance of Dataset OR a subclass of Dataset
        
        Parameter centroid: the centroid point (which might not be a point in ds)
        Precondition: centroid is a list of numbers (int or float),
          len(centroid) = ds.getDimension()
        """
        # IMPLEMENT ME
        assert isinstance(ds, Dataset) or issubclass(ds, Dataset)
        assert is_point(centroid) and len(centroid) == ds.getDimension()
        self._dataset = ds
        self._centroid = centroid[:]
        self._indices = []


    def getCentroid(self):
        """Returns: the centroid of this cluster.
        
        This getter method is to protect access to the centroid.
        """
        return self._centroid
  
    
    def getIndices(self):
        """Returns: the indices of points in this cluster
        
        This method returns the attribute _indices directly.  Any changes
        made to this list will modify the cluster.
        """
        return self._indices
   
    
    def addIndex(self, index):
        """Adds the given dataset index to this cluster.
        
        If the index is already in this cluster, then this method leaves the
        cluster unchanged.
        
        Parameter index: the index of the point to add
        Precondition: index is a valid index into this cluster's dataset.
        That is, index is an int in the range 0.._dataset.getSize()-1.
        """
        assert type(index) == int and 0 <= index < self._dataset.getSize()
        if not index in self. _indices:
            self._indices.append(index)
 
    
    def clear(self):
        """Removes all points from this cluster, but leave the centroid unchanged.
        """
        self._indices=[]
 
    
    def getContents(self):
        """Returns: a new list containing copies of the points in this cluster.
        
        The result is a list of list of numbers.  It has to be computed from
        the indices.
        """
        newlist = []
        for x in self._indices:
            newlist.append(self._dataset.getContents()[x][:])
        return newlist
    
    
    # Part B
    def distance(self, point):
        """Returns: The euclidean distance from point to this cluster's centroid.
        
        Parameter point: the point to compare to this cluster's centroid
        Precondition: point is a list of numbers (int or float),
          len(point) = _ds.getDimension()
        """
        assert is_point(point) and len(point) == self._dataset.getDimension()
        sum = 0
        for x in range(len(point)):
            sum = sum + (point[x]-self._centroid[x])**2
        return math.sqrt(float(sum))
    
    def updateCentroid(self):
        """Returns: Trues if the centroid remains unchanged; False otherwise.
        
        This method recomputes the _centroid attribute of this cluster. The
        new _centroid attribute is the average of the points of _contents
        (To average a point, average each coordinate separately).  
        
        Whether the centroid "remained the same" after recomputation is determined 
        by the function numpy.allclose().  The return value should be interpreted
        as an indication of whether the starting centroid was a "stable" position 
        or not.
        
        If there are no points in the cluster, the centroid. does not change.
        """
        old_centroid = self._centroid
        if self._indices == []:
            return True
        new_centroid = []
        old_contents = self.getContents()
        for x in range(self._dataset.getDimension()):
            sum = 0
            for y in range(len(old_contents)):
                sum = sum+ old_contents[y][x]
            sum = sum/float(len(old_contents))
            new_centroid.append(sum)
        self._centroid = new_centroid
        return numpy.allclose(old_centroid,self._centroid)
    
    
    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """Returns: String representation of the centroid of this cluster."""
        return str(self._centroid)
 
   
    def __repr__(self):
        """Returns: Unambiguous representation of this cluster. """
        return str(self.__class__) + str(self)


class ClusterGroup(object):
    """An instance is a set of clusters of the points in a dataset.
    
    Instance Attributes:
        _dataset: the dataset which this is a clustering of     [Dataset]
        
        _clusters: the clusters in this clustering (not empty)  [list of Cluster]
    """
    
    
    # Part A
    def __init__(self, ds, k, seed_inds=None):
        """Initializer: Creates a clustering of the dataset ds into k clusters.
        
        The clusters are initialized by randomly selecting k different points
        from the database to be the centroids of the clusters.  If seed_inds
        is supplied, it is a list of indices into the dataset that specifies
        which points should be the initial cluster centroids.
        
        IMPORTANT: READ THE PRECONDITION OF ds VERY CAREFULLY
        
        Parameter ds: the Dataset for this cluster group
        Precondition: ds is a instance of Dataset OR a subclass of Dataset
        
        Parameter k: The number of clusters (the k in k-means)
        Precondition: k is an int, 0 < k <= ds.getSize()
        
        Parameter seed_inds: the INDEXES of the points to start with
        Precondition: seed_inds is None, or a list of k valid indices into ds.
        """
        assert isinstance(ds, Dataset) or issubclass(ds, Dataset)
        assert type(k)==int and 0 < k <= ds.getSize()
        assert is_k_list(seed_inds,ds)
        self._dataset = ds
        if seed_inds is None:
            centroids = random.sample(ds.getContents(),k)
        else:
            centroids = []
            for x in seed_inds:
                newpoint = ds.getPoint(x)
                centroids.append(newpoint)
        self._clusters = []
        for x in centroids:
            newcluster = Cluster(ds,x)
            self._clusters.append(newcluster)
        
    
    def getClusters(self):
        """Returns: The list of clusters in this object.
        
        This method returns the attribute _clusters directly.  Any changes
        made to this list will modify the set of clusters.
        """ 
        return self._clusters


    # Part B
    def _nearest_cluster(self, point):
        """Returns: Cluster nearest to point
    
        This method uses the distance method of each Cluster to compute the distance 
        between point and the cluster centroid. It returns the Cluster that is 
        the closest.
        
        Ties are broken in favor of clusters occurring earlier in the list of 
        self._clusters.
        
        Parameter point: the point to match
        Precondition: point is a list of numbers (int or float),
          len(point) = self._dataset.getDimension().
        """
        assert is_point(point) and len(point) == self._dataset.getDimension()
        result = self._clusters[0]
        for x in range(len(self._clusters)):
            nearest = result.distance(point)
            if self._clusters[x].distance(point) < nearest:
                result = self._clusters[x]
        return result
           
    
    def _partition(self):
        """Repartitions the dataset so each point is in exactly one Cluster.
        """
        # First, clear each cluster of its points.  Then, for each point in the
        # dataset, find the nearest cluster and add the point to that cluster.
        for x in self._clusters:
            x.clear()
        for y in range(len(self._dataset.getContents())):
            nearest = self._nearest_cluster(self._dataset.getContents()[y])
            nearest.getIndices().append(y)
    
    
    # Part C
    def _update(self):
        """Returns:True if all centroids are unchanged after an update; False otherwise.
        
        This method first updates the centroids of all clusters'.  When it is done, it
        checks whether any of them have changed. It then returns the appropriate value.
        """
        okay = True
        for x in self._clusters:
            result = x.updateCentroid()
            if result == False:
                okay = False
        return okay
            
    
    def step(self):
        """Returns: True if the algorithm converges after one step; False otherwise.
        
        This method performs one cycle of the k-means algorithm. It then checks if
        the algorithm has converged and returns True or False
        """
        # In a cycle, we partition the points and then update the means.
        # IMPLEMENT ME
        self._partition()
        result = self._update()
        return result
    
    
    # Part D
    def run(self, maxstep):
        """Continues clustering until either it converges or reaches maxstep steps.
        
        The stopping condition (convergence, maxsteps) is whichever comes first.
        
        Precondition maxstep: Maximum number of steps before giving up
        Precondition: maxstep is int >= 0.
        """
        # Call step repeatedly, up to maxstep times, until the algorithm
        # converges.  Stop after maxstep iterations even if the algorithm has not
        # converged.
        
        # IMPLEMENT ME
        assert type(maxstep) == int and maxstep >= 0
        i = 0
        while i <= maxstep or step_result == False:
            self.step()
            step_result = self.step()
            i = i + 1
    
    
    # PROVIDED METHODS: Do not modify!
    def __str__(self):
        """Returns: String representation of the centroid of this cluster."""
        return str(self._clusters)
    
    
    def __repr__(self):
        """Returns: Unambiguous representation of this cluster. """
        return str(self.__class__) + str(self)

