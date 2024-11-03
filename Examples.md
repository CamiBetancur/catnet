# Usage examples


```python
import catnet
```

## Create networks from literature review tables

### Example 1: Literature review data table with a "long" format

A long dataframe contains one entry of the category variable in one row. For instance, you can see that the following table, `long_df`, has an `impact_cats` columns. In this example, `impact_cats` is the variable to be transformed into a network. Note that for each id (`publication` column), there are many rows, each containing a different `impact_cats` value.


```python
long_df = catnet.test_data(dataset="long")

long_df.head(5)
```





<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>publication</th>
      <th>year</th>
      <th>title</th>
      <th>impact</th>
      <th>impact_cats</th>
      <th>other_info</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kumar-Reddy (2004)</td>
      <td>2005</td>
      <td>The Role of Gender in Urban Mobility Sustainab...</td>
      <td>Significant mobility improvements for women in...</td>
      <td>Environmental impact</td>
      <td>[additional data may be available]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Kumar-Reddy (2004)</td>
      <td>2005</td>
      <td>The Role of Gender in Urban Mobility Sustainab...</td>
      <td>Significant mobility improvements for women in...</td>
      <td>Decreased travel time</td>
      <td>[additional data may be available]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kumar-Reddy (2004)</td>
      <td>2005</td>
      <td>The Role of Gender in Urban Mobility Sustainab...</td>
      <td>Significant mobility improvements for women in...</td>
      <td>Women's empowerment</td>
      <td>[additional data may be available]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ivanov-Petrov (2024)</td>
      <td>2024</td>
      <td>Gender-Based Inequalities in Sustainable Trans...</td>
      <td>Holistic improvements in gender representation...</td>
      <td>Mobility justice</td>
      <td>[additional data may be available]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Ivanov-Petrov (2024)</td>
      <td>2024</td>
      <td>Gender-Based Inequalities in Sustainable Trans...</td>
      <td>Holistic improvements in gender representation...</td>
      <td>Women's empowerment</td>
      <td>[additional data may be available]</td>
    </tr>
  </tbody>
</table>
</div>



To transform the above literature review table into a network, using the categories from the `impact_cats` column, you can use the function `from_long_df()`. To do this, you must provide an `id_col`, which identifies to which document document each connection between categories belong to (in which document categories coexist). The `var_col` column contains the categories to be transformed into a Network.

The `from_long_df()` function returns a Network object, as the next cell shows.


```python
net = catnet.from_long_df(long_df,
                            id_col="publication",
                            var_col="impact_cats")

net
```




    Network(nodelist cols: ['id', 'label']
    	edgelist cols: ['id', 'source', 'target']
    )



You can explore the edges and the nodes by accessing the `edgelist` and `nodelist` attributes of the `Network` class variable, as shown in the following code cells (note that the `head(5)` method is added to limit the code cell size and avoid saturation in this document):


```python
net.edgelist.head(5)
```





<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>source</th>
      <th>target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kumar-Reddy (2004)</td>
      <td>Environmental impact</td>
      <td>Decreased travel time</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Kumar-Reddy (2004)</td>
      <td>Environmental impact</td>
      <td>Women's empowerment</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kumar-Reddy (2004)</td>
      <td>Decreased travel time</td>
      <td>Women's empowerment</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ivanov-Petrov (2024)</td>
      <td>Mobility justice</td>
      <td>Women's empowerment</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Ivanov-Petrov (2024)</td>
      <td>Mobility justice</td>
      <td>LGBTQ+ accessibility</td>
    </tr>
  </tbody>
</table>
</div>




```python
net.nodelist.head(5)
```





<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Gender-neutral policies</td>
      <td>Gender-neutral policies</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Employment access</td>
      <td>Employment access</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Decreased travel time</td>
      <td>Decreased travel time</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Mobility justice</td>
      <td>Mobility justice</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Reduced gender gap</td>
      <td>Reduced gender gap</td>
    </tr>
  </tbody>
</table>
</div>



Also, by using the method `with_weigths` of the `EdgeList` class, you can generate an edgelist table with weights:


```python
net.edgelist.with_weights(ordered="descending").head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>source</th>
      <th>target</th>
      <th>weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>Community participation</td>
      <td>LGBTQ+ accessibility</td>
      <td>3</td>
    </tr>
    <tr>
      <th>41</th>
      <td>Women's empowerment</td>
      <td>Equity focus</td>
      <td>2</td>
    </tr>
    <tr>
      <th>45</th>
      <td>Women's empowerment</td>
      <td>LGBTQ+ accessibility</td>
      <td>2</td>
    </tr>
    <tr>
      <th>44</th>
      <td>Women's empowerment</td>
      <td>Infrastructure improvements</td>
      <td>2</td>
    </tr>
    <tr>
      <th>43</th>
      <td>Women's empowerment</td>
      <td>Increased safety</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>



### Example 2: Literature review data table with the categories contained in a single cell ("same_cell" data)

If your literature review table contains a list of categories inside the same cell, you have a "same_cell" data frame. The list of categories can use linebreaks ("\r\n"), hyphens used as bullet points ("- "), or semicolons (";") as list separators. The following cell preesents an example of this, using hyphens and linebreaks as separators (`impact_cats` column):


```python
same_cell_df = catnet.test_data("same_cell")

same_cell_df.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>publication</th>
      <th>year</th>
      <th>title</th>
      <th>impact</th>
      <th>impact_cats</th>
      <th>other_info</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kumar-Reddy (2004)</td>
      <td>2005</td>
      <td>The Role of Gender in Urban Mobility Sustainab...</td>
      <td>Significant mobility improvements for women in...</td>
      <td>- Environmental impact\r\n- Decreased travel t...</td>
      <td>[additional data may be available]</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Ivanov-Petrov (2024)</td>
      <td>2024</td>
      <td>Gender-Based Inequalities in Sustainable Trans...</td>
      <td>Holistic improvements in gender representation...</td>
      <td>- Mobility justice\r\n- Women's empowerment\r\...</td>
      <td>[additional data may be available]</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Okafor-Ademola (2014)</td>
      <td>2006</td>
      <td>Gendered Challenges in Accessing Public Transi...</td>
      <td>Enhanced safety and inclusivity for queer indi...</td>
      <td>- Improved access\r\n- Sustainable transport use</td>
      <td>[additional data may be available]</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Okafor-Ademola (2017)</td>
      <td>2018</td>
      <td>Impact of Public Transportation on Gender Equi...</td>
      <td>Gender-sensitive policies improved overall sat...</td>
      <td>- Women's empowerment\r\n- Increased safety\r\...</td>
      <td>[additional data may be available]</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Tanaka-Sato (2016)</td>
      <td>2002</td>
      <td>The Role of Gender in Urban Mobility Sustainab...</td>
      <td>Reduction of gender-based mobility gaps in urb...</td>
      <td>- Employment access\r\n- Infrastructure improv...</td>
      <td>[additional data may be available]</td>
    </tr>
  </tbody>
</table>
</div>



To transform these literature review tables into category networks, you can use the `from_same_cell()` function, as following:


```python
net = catnet.from_same_cell(same_cell_df, 
                              id_col="publication", 
                              var_col="impact_cats", 
                              sep="- ")

net
```




    Network(nodelist cols: ['id', 'label']
    	edgelist cols: ['id', 'source', 'target']
    )



Like Example 1, you can inspect the edgelist and nodelist of the `Network` object:


```python
net.edgelist.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>source</th>
      <th>target</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Kumar-Reddy (2004)</td>
      <td>Environmental impact</td>
      <td>Decreased travel time</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Kumar-Reddy (2004)</td>
      <td>Environmental impact</td>
      <td>Women's empowerment</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Kumar-Reddy (2004)</td>
      <td>Decreased travel time</td>
      <td>Women's empowerment</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Ivanov-Petrov (2024)</td>
      <td>Mobility justice</td>
      <td>Women's empowerment</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Ivanov-Petrov (2024)</td>
      <td>Mobility justice</td>
      <td>LGBTQ+ accessibility</td>
    </tr>
  </tbody>
</table>
</div>




```python
net.nodelist.head(5)
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>id</th>
      <th>label</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Gender-neutral policies</td>
      <td>Gender-neutral policies</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Inclusivity measures</td>
      <td>Inclusivity measures</td>
    </tr>
    <tr>
      <th>2</th>
      <td>LGBTQ+ accessibility</td>
      <td>LGBTQ+ accessibility</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Increased safety</td>
      <td>Increased safety</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Decreased travel time</td>
      <td>Decreased travel time</td>
    </tr>
  </tbody>
</table>
</div>



## Export network to Gephi

You can export the `Network.edgelist` and `Network.nodelist` objects to .csv files ready to be used by Gephi. To do this, you can use the `Network.to_gephi()` method. This will produce a folder with the name you choose, following "_gephi", in the directory path you choose (`path` attribute of the method). Inside this folder, you will find a .csv for the edgelist and a .csv for the nodelist of your Network.


```python
net.to_gephi(name="literature_review")
```
