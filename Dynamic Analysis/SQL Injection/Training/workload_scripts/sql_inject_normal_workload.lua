require "socket"
math.randomseed(socket.gettime()*1000)
math.random(); math.random(); math.random()

request = function()
  local method = "POST"
  -- Use your cluster-ip here:
  local path = "http://10.10.1.201:8082/api/sqlquery"
  local headers = {}
  headers["Content-Type"] = "application/json;charset=UTF-8"
  local x = math.random(1,1000000)
  local body1 = [[ {"user_id":"SELECT first_name,last_name FROM users where user_id = ]]
  local body2 = [["} ]]
  local body = body1..x..body2
  return wrk.format(method, path, headers, body)
end