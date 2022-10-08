let usages: number[] = [];

let index = 0;

for (let i = 0; i < 100; i++) {
  usages.push(Math.floor(Math.random() * 100) + 100);
}

export function mostRecentUsage() {
  return usages[index++];
}
