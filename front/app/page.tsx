import Dropzone from './dropzone/page';
import Masked from './masked/page';

export default function Home() {
  return (
    <div className="m-4">
      <h1 className="text-2xl">植物を検出する</h1>
      <Dropzone />
      <Masked />
    </div>
  );
}