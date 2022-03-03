require "socket"
math.randomseed(socket.gettime()*1000)
math.random(); math.random(); math.random()

request = function()
  local method = "POST"
  -- Use your cluster-ip here:
  local path = "http://10.10.1.201:8080/api/v1/travelservice/trips/left"
  local headers = {}
  headers["Content-Type"] = "application/json;charset=UTF-8"
  local body = [[ {"startingPlace":"Nan Jing","endPlace":"Shang Hai","departureTime":"2020-03-07"} ]]
  return wrk.format(method, path, headers, body)
end