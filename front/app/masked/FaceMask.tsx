

const FaceMask = async () => {
  await new Promise((resolve) => setTimeout(resolve, 5000));
  const response = await fetch('https://3000--main--webapp--kensukemiyata.code.webfrontier.co.jp/api');
  if (!response.ok) throw new Error('Failed to fetch data');
};
  
export default FaceMask;