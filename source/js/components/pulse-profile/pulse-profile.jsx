import React from "react";

const PulseProfile = ({ profile }) => {
  return (
    <div className="tw-grid tw-grid-cols-4 tw-grid-rows-3 large:tw-grid-cols-5 tw-gap-x-3 tw-gap-y-2 tw-border-t tw-border-black">
      {/* Image */}
      <a
        href={`https://www.mozillapulse.org/profile/${profile.profile_id}`}
        className="tw-block tw-row-span-1 large:tw-row-span-4 tw-col-span-1 tw-relative tw-min-h-[160px] tw-h-[100%] tw-w-full tw-overflow-hidden"
      >
        <img
          src={
            profile.thumbnail
              ? profile.thumbnail
              : "static/_images/fellowships/headshot/placeholder.jpg"
          }
          className="tw-w-auto tw-h-full tw-absolute tw-left-50 tw-top-50 tw-min-w-full tw-object-cover"
          alt="Headshot"
        />
      </a>

      {/* Right card  */}
      <div className="tw-row-span-1 large:tw-row-span-1 tw-col-span-3 large:tw-col-span-4">

        {/* Card top */}
        <div className="tw-flex tw-flex-row tw-justify-between tw-items-center tw-mt-2">
          <a
            className="h5-heading tw-mb-1 tw-font-sans tw-font-normal"
            href={`https://www.mozillapulse.org/profile/${profile.profile_id}`}
          >
            {profile.name}
          </a>

          {/* Social Icons */}
          <div className="tw-flex tw-flex-row tw-space-x-2">
            {profile.twitter && (
              <a
                href={profile.twitter}
                className="twitter twitter-glyph small"
              />
            )}
            {profile.linkedin && (
              <a
                href={profile.linkedin}
                className="linkedIn linkedIn-glyph small"
              />
            )}
          </div>
        </div>

        {/* Profile Location */}
        {profile.location && (
          <p className="tw-flex-row tw-flex tw-items-center tw-justify-start">
            <img
              className="tw-w-[12px] tw-h-[12px] tw-block tw-mr-1 body-small"
              src="static/_images/glyphs/map-marker-icon.svg"
              alt=""
            />
            {profile.location}
          </p>
        )}
      </div>

      {/* Short bio block */}
      <div className="large:tw-row-span-2 tw-col-span-4 large:tw-col-start-2 large:tw-col-span-4">
        <p className="tw-text-gray-60">{profile.user_bio}</p>

        {profile.program_type && (
          <div className="tw-flex tw-flex-wrap tw-mt-auto">
            <span className="tw-text-blue tw-text-sm tw-font-bold first:tw-ml-0 tw-ml-2">
              {profile.program_type}
            </span>
          </div>
        )}
      </div>
    </div>
  );
};

export default PulseProfile;