#!/usr/bin/node

const request = require('request');
const args = process.argv;
const argument = args[2];

async function fetchData() {
  try {
    const response = await new Promise((resolve, reject) => {
      request.get(`https://swapi-api.alx-tools.com/api/films/${argument}`, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          resolve({ response, body });
        }
      });
    });

    const data = JSON.parse(response.body);
    const names = data.characters;

    const charactersData = await Promise.all(names.map(async (name) => {
      try {
        const characterResponse = await new Promise((resolve, reject) => {
          request.get(name, (error, response, body) => {
            if (error) {
              reject(error);
            } else {
              resolve({ response, body });
            }
          });
        });
        return JSON.parse(characterResponse.body).name;
      } catch (error) {
        console.error(error);
        return null;
      }
    }));
    charactersData.map((char) => {
      console.log(char)
    })
  } catch (error) {
    console.error(error);
  }
}

fetchData();