function validationFailed () {
  echo "Usage: ./release-add-tickets.sh versionString tickets"
  echo "versionString - required - semver string e.g. 1.2.3"
  echo "tickets       - required - comma separated list of ticket numbers e.g. ABC-123, ABC-124"
  exit
}

versionString=$1
tickets=$2

if [[ "$versionString" == "" ]]; then
  validationFailed
fi

if [[ "$tickets" == "" ]]; then
  validationFailed
fi

ticketCount=`echo "$tickets"|awk -F',' '{print NF}'`

echo "Successfully added $ticketCount tickets to release for version $versionString"