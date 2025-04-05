export function generateTestUser() {
    const firstNames = ['Jan', 'Petr', 'Lucie', 'Anna', 'Tomáš'];
    const lastNames = ['Novák', 'Svoboda', 'Dvořák', 'Procházka', 'Černý'];
    const zipCodes = ['10000', '11000', '12000', '13000', '14000'];
  
    const firstName = firstNames[Math.floor(Math.random() * firstNames.length)];
    const lastName = lastNames[Math.floor(Math.random() * lastNames.length)];
    const zip = zipCodes[Math.floor(Math.random() * zipCodes.length)];
  
    return {
      firstName,
      lastName,
      zip
    };
  }
  