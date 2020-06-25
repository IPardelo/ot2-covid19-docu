#!/bin/bash


# -------------------------------------------------------------------------------------------------------
# Script Name: update-all-robots-library.sh
#
# Author: Luis Lorenzo Mosquera, Víctor Soroña Pombo & Ismael Castiñeira Paz
#
# Date : June 12th 2020
#
# Description: The following script updates ot2 libraries in specified input parameters 
#
# Error Log: Any errors or output associated with the script can be found in standard output
# 
# License: GPL-3.0
# -------------------------------------------------------------------------------------------------------

# -------------------------
# Install requirements
# -------------------------
# sudo apt install -y sshpass ssh-agent openssh-client

# -------------------------
# Constants
# -------------------------
IP='192.168.167.'
export SSHPASS='L@b0r4t010'
PUBLIC_KEY_PATH='~/ot-ssh-key'
LOCAL_LIBRARY_PATH='/home/luis/Escritorio/ot2-covid19'
ROBOT_RP_USER='root'
ROBOT_LIBRARY_PATH='/root'

SARS=(${IP}'51' ${IP}'52')
SBRS=(${IP}'54' ${IP}'55' ${IP}'56')
SCRS=(${IP}'58' ${IP}'59')

ALL_ROBOTS=("${SARS[@]}" "${SBRS[@]}" "${SCRS[@]}")


# -------------------------
# Input processing
# -------------------------
if [[ $1 == "a" ]]; then
    printf "Updating A robots\n\n"
    TARGETS=("${SARS[@]}")
elif [[ $1 == "b" ]]; then
    printf "Updating B robots\n\n"
    TARGETS=("${SBRS[@]}")
elif [[ $1 == "c" ]]; then
    printf "Updating C robots\n\n"
    TARGETS=("${SCRS[@]}")
else
    printf "Updating all robots\n\n"
    TARGETS=("${ALL_ROBOTS[@]}")
fi


# -------------------------
# Updating loop
# -------------------------
for robot_ip in "${TARGETS[@]}"; do
   echo "updating ~> $robot_ip"
   sshpass -e scp -i $PUBLIC_KEY_PATH -r $LOCAL_LIBRARY_PATH $ROBOT_RP_USER@$robot_ip:$ROBOT_LIBRARY_PATH
done
