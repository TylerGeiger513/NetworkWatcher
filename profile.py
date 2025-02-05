#!/usr/bin/env python3
import geni.portal as portal
import geni.rspec.pg as pg

# Create a portal context
pc = portal.Context()

# Create an RSpec object
rspec = pg.Reservation()

# Add a node with your desired configuration
node = rspec.AddNode("node1")
node.hardware_type = "emulab-base"
node.disk_image = "urn:publicid:IDN+emulab.net+image+debian10-64-minimal"

# Add a startup service that clones your Git repository and runs monitor.sh
node.addService(pg.Execute(shell="bash", command="""
  cd /local
  if [ ! -d repository ]; then
    git clone https://github.com/TylerGeiger513/NetworkWatcher.git repository
  else
    cd repository && git pull
  fi
  bash repository/monitor.sh &
"""))

# Output the generated RSpec
portal.context.printRequestRSpec(rspec)
