Lazy evaulation means that Spark will wait until the very last moment to execute the graph of computation instructions.</br>

In Spark, instead of modifying the data immediately when you express some operation, you build up a plan of transformations</br>
that you would like to apply to your source data.</br>

By waiting until the last minute to execute the code, Spark compiles this plan from your raw DataFrame transformations</br>
to a streamlined physical plan that will run as efficiently as possible across the cluster.</br>

This provides immense benefits because Spark can optimize the entire data flow from end to end.
