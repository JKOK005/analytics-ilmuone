function res = GetCountry(conn, code)
  txt   = sprintf(" SELECT * FROM countries WHERE \
                    code='%s' ", code);
  
  res   = pq_exec_params(conn, txt);
  res   = res.data;
end
  