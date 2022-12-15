def TestProc1():
  # Create a query
  Qry = ADO.CreateADOQuery()
  # Specify the connection string
  Qry.ConnectionString = f"Driver=PostgreSQL ANSI;Data Source= PostgreSQL30;Server=10.244.172.6;Port=5432;Database=hfi_consumable;UserName=postgres;Password=postgres;"
  # Specify the SQL expression
  Qry.SQL = "SELECT DISTINCT instrument_id FROM public.reagent_container WHERE instrument_id = '40e6215d-b5c6-4896-987c-f30f3678f601'"
  # Specify the parameter value
  #Qry.Parameters.ParamByName("Param_State").Value = "Canada"
  # Execute the query
  Qry.Open()
  # Process results and insert data into the test log
  Log.AppendFolder("Customers from Canada")
  Qry.First()
  Log.Message(Qry.FieldByName("instrument_id").Value)
  aqObject.CompareProperty(Qry.FieldByName("instrument_id").Value,cmpEqual, '40e6215d-b5c6-4896-987c-f30f3678f601',True, lmError)