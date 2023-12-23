from typing import List, Any, Optional
import datetime

from .models import _BaseModel


class Root(_BaseModel):
    releases: List["Release"]
    accountOnboardingSteps: List["AccountOnboardingStep"]
    account: "Account"
    loggedInUser: "User"
    cardsStatusHistory: List["CardsStatusHistory"]
    cardsEffortHistory: List["CardsEffortHistory"]
    cardsFinishedHistory: List["CardsFinishedHistory"]
    cardsTimeToFinished: List["CardsTimeToFinished"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AccountOnboardingStep(_BaseModel):
    chapter: str
    description: str
    milestone: str
    sortValue: str
    title: str
    variants: list
    xp: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AccountOnboarding(_BaseModel):
    account: "Account"
    steps: str
    variants: list

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AccountRole(_BaseModel):
    account: "Account"
    createdAt: datetime.datetime
    isBillingContact: str
    lastChangedAt: datetime.datetime
    role: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AccountSetting(_BaseModel):
    account: "Account"
    key: str
    usesDefault: str
    value: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AccountUserAchievement(_BaseModel):
    account: "Account"
    context: str
    user: "User"
    value: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AccountUserSetting(_BaseModel):
    account: "Account"
    inboxDeck: "Deck"
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Account(_BaseModel):
    activeFeatureFlags: str
    activeProjectCount: int
    allowInheritHeroCover: bool
    attachmentCoverMode: str
    billingCity: str
    billingCountryCode: str
    billingLine1: str
    billingLine2: str
    billingName: str
    billingType: str
    billingZip: str
    coupon: str
    createdAt: datetime.datetime
    dependenciesEnabled: bool
    disabledAt: datetime.datetime
    disabledBy: "User"
    effortScale: str
    hideCompletedCardCountForDecks: bool
    id: str
    isDisabled: bool
    isLearning: bool
    isNonProfit: bool
    maxHandSlotCount: int
    maxTimeTrackingSegmentMsDuration: int
    milestonesEnabled: bool
    name: str
    netGiftAmount: str
    offeringTrial: bool
    persona: str
    priorityLabels: str
    seats: int
    staffPermission: str
    statusChangeDurations: str
    subdomain: str
    timeTrackingMode: str
    timeTrackingSwimLaneInfo: bool
    totalMediaByteUsage: int
    workdays: str
    workflowMode: str
    cards: List["Card"]
    invoices: List["Invoice"]
    cardPresets: List["CardPreset"]
    attachments: List["Attachment"]
    discordGuilds: List["DiscordGuild"]
    timeTrackingSegments: List["TimeTrackingSegment"]
    workflowItems: List["WorkflowItem"]
    deckAssignments: List["DeckAssignment"]
    assigneeAssignments: List["AssigneeAssignment"]
    assigneeDeckAssignments: List["AssigneeDeckAssignment"]
    wizards: List["Wizard"]
    milestones: List["Milestone"]
    handCards: List["HandCard"]
    resolvables: List["Resolvable"]
    cardUpvotes: List["CardUpvote"]
    resolvableParticipants: List["ResolvableParticipant"]
    userReportSettings: List["UserReportSetting"]
    cardOrders: List["CardOrder"]
    accountUserAchievements: List["AccountUserAchievement"]
    userInviteCodes: List["UserInviteCode"]
    decks: List["Deck"]
    queueEntries: List["QueueEntry"]
    anyDecks: List["Deck"]
    projects: List["Project"]
    archivedProjects: List["Project"]
    anyProjects: List["Project"]
    onboardingDeck: "Deck"
    deckSubscriptions: List["DeckSubscription"]
    roles: List["AccountRole"]
    invitations: List["UserInvitation"]
    githubIntegration: "Integration"
    slackIntegration: "Integration"
    affiliateCodes: List["AffiliateCode"]
    activities: List["Activity"]
    stripeAccountSync: "StripeAccountSync"
    accountOnboarding: "AccountOnboarding"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ActiveTimeTracker(_BaseModel):
    account: "Account"
    card: "Card"
    createdAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Activity(_BaseModel):
    card: "Card"
    changer: "User"
    createdAt: datetime.datetime
    data: str
    deck: "Deck"
    isRemovedFromDeckEntry: bool
    isRemovedFromMilestoneEntry: bool
    milestone: "Milestone"
    project: "Project"
    type: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AffiliateCodeStat(_BaseModel):
    affiliateCode: "AffiliateCode"
    month: int
    newVisitors: int
    revenue: int
    signups: int
    visits: int
    year: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AffiliateCode(_BaseModel):
    account: "Account"
    code: str
    createdAt: datetime.datetime
    creator: "User"
    isDeleted: bool
    isDisabled: bool
    label: str
    message: str
    remainingRedemptions: int
    reward: str
    validUntil: Any
    vanityUrl: str
    stats: List["AffiliateCodeStat"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AssigneeAssignment(_BaseModel):
    account: "Account"
    assignedBy: "User"
    assignee: "User"
    lastAssignedAt: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AssigneeDeckAssignment(_BaseModel):
    account: "Account"
    assignedBy: "User"
    assignee: "User"
    deck: "Deck"
    lastAssignedAt: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Attachment(_BaseModel):
    account: "Account"
    card: "Card"
    content: str
    createdAt: datetime.datetime
    creator: "User"
    file: "File"
    title: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardDiffNotification(_BaseModel):
    account: "Account"
    asOwner: bool
    card: "Card"
    changers: list
    changes: str
    createdAt: datetime.datetime
    lastUpdatedAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardHistory(_BaseModel):
    account: "Account"
    card: "Card"
    changer: "User"
    diff: str
    version: int
    versionCreatedAt: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardOrderInDeck(_BaseModel):
    card: "Card"
    changer: "User"
    deck: "Deck"
    sortIndex: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardOrder(_BaseModel):
    account: "Account"
    card: "Card"
    label: str
    sortValue: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardPreset(_BaseModel):
    account: "Account"
    createdAt: datetime.datetime
    creator: "User"
    data: str
    name: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardSubscription(_BaseModel):
    card: "Card"
    createdAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardUpvote(_BaseModel):
    account: "Account"
    card: "Card"
    createdAt: datetime.datetime
    discordUserInfo: str
    type: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Card(_BaseModel):
    account: "Account"
    accountSeq: str
    assignee: "User"
    checkboxInfo: list
    checkboxStats: str
    content: str
    coverFile: "File"
    createdAt: datetime.datetime
    creator: "User"
    deck: "Deck"
    discordGuild: "DiscordGuild"
    dueDate: datetime.datetime
    effort: Any
    embeds: str
    hasBlockingDeps: bool
    isDoc: bool
    isPublic: bool
    lastUpdatedAt: datetime.datetime
    legacyProject: "Project"
    legacyProjectSeq: int
    masterTags: list
    mentionedUsers: list
    meta: str
    milestone: "Milestone"
    parentCard: "Card"
    priority: str
    sourceWorkflowItemId: "WorkflowItem"
    status: str
    tags: list
    title: str
    version: str
    visibility: str
    resolvables: List["Resolvable"]
    handCards: List["HandCard"]
    timeTrackingSegments: List["TimeTrackingSegment"]
    cardSubscriptions: List["CardSubscription"]
    resolvableEntries: List["ResolvableEntry"]
    attachments: List["Attachment"]
    diffs: List["CardHistory"]
    totalTimeTrackingSums: "TimeTrackingSum"
    userTimeTrackingSums: List["TimeTrackingSum"]
    childCards: List["Card"]
    inDeps: List["Card"]
    outDeps: List["Card"]
    cardReferences: List["Card"]
    upvotes: List["CardUpvote"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardsEffortHistory(_BaseModel):
    cardCount: int
    date: datetime.datetime
    effortSum: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardsFinishedHistory(_BaseModel):
    assignee: "User"
    cardCount: int
    date: datetime.datetime
    effortSum: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardsStatusHistory(_BaseModel):
    count: int
    date: datetime.datetime
    status: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardsTimeToFinished(_BaseModel):
    assignee: "User"
    card: "Card"
    doneAt: datetime.datetime
    effort: int
    startedAt: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DailyDiscordGuildVoteMembership(_BaseModel):
    discordGuild: "DiscordGuild"
    membershipCount: int
    t: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DailyPublicProjectMembership(_BaseModel):
    membershipCount: int
    project: "Project"
    t: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class PublicProjectVisit(_BaseModel):
    project: "Project"
    t: datetime.datetime
    topReferrers: str
    visitCounts: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DeckAssignment(_BaseModel):
    account: "Account"
    deck: "Deck"
    lastAssignedAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DeckOrder(_BaseModel):
    deck: "Deck"
    project: "Project"
    sortIndex: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DeckPublicOrder(_BaseModel):
    deck: "Deck"
    project: "Project"
    sortIndex: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DeckSubscription(_BaseModel):
    deck: "Deck"
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Deck(_BaseModel):
    account: "Account"
    accountSeq: int
    content: str
    coverColor: str
    coverFile: "File"
    createdAt: datetime.datetime
    creator: "User"
    defaultCard: str
    defaultProjectTag: "ProjectTag"
    handSyncEnabled: bool
    isDeleted: bool
    isOnboardingDeck: bool
    manualOrderLabels: str
    milestone: "Milestone"
    preferredOrder: Any
    project: "Project"
    stats: str
    stickyDefaultProjectTag: bool
    title: str
    cards: List["Card"]
    workflowItems: List["WorkflowItem"]
    cardOrderInDecks: List["CardOrderInDeck"]
    activities: List["Activity"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DiscordGuild(_BaseModel):
    account: "Account"
    createdAt: datetime.datetime
    discordGuildId: str
    guildIconId: str
    guildName: str
    karmaRoleThresholds: str
    removeCommandEmoji: str
    removeCommandEnabled: str
    removeCommandRoleId: str
    scope: str
    slashCommands: List["DiscordSlashCommand"]
    projectNotifications: List["DiscordProjectNotification"]
    dailyDiscordGuildVoteMemberships: List["DailyDiscordGuildVoteMembership"]
    members: List["DiscordMember"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DiscordMember(_BaseModel):
    avatar: str
    createdAt: datetime.datetime
    deckyScore: int
    discordGuild: "DiscordGuild"
    discordUserId: str
    discriminator: str
    name: str
    nick: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DiscordProjectNotification(_BaseModel):
    createdAt: datetime.datetime
    disabledTypes: str
    discordChannelId: str
    discordGuild: "DiscordGuild"
    project: "Project"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DiscordSlashCommand(_BaseModel):
    autoAddRoleToThread: str
    channelId: str
    deck: "Deck"
    description: str
    discordGuild: "DiscordGuild"
    karmaForCompletion: int
    leaderboard: str
    name: str
    permissions: str
    reaction: str
    reactionThreshold: int
    statusMessages: str
    statusTargetChannelId: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DueCard(_BaseModel):
    account: "Account"
    card: "Card"
    createdAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class File(_BaseModel):
    account: "Account"
    createdAt: datetime.datetime
    deletedAt: datetime.datetime
    deletedBy: "User"
    isDeleted: bool
    meta: str
    name: str
    selfHosted: bool
    size: str
    uploader: "User"
    url: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class HandCard(_BaseModel):
    account: "Account"
    card: "Card"
    sortIndex: int
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Integration(_BaseModel):
    account: "Account"
    createdAt: datetime.datetime
    creator: "User"
    disabled: str
    type: str
    user: "User"
    userData: str
    version: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Invoice(_BaseModel):
    account: "Account"
    chargeData: str
    charged: int
    createdAt: datetime.datetime
    invoiceNumber: str
    subtotal: int
    total: int
    url: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class LastSeenCardUpvote(_BaseModel):
    account: "Account"
    createdAt: datetime.datetime
    lastSeenAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class MilestoneProgress(_BaseModel):
    milestone: "Milestone"
    progress: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class MilestoneProject(_BaseModel):
    account: "Account"
    milestone: "Milestone"
    project: "Project"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Milestone(_BaseModel):
    account: "Account"
    accountSeq: int
    color: str
    createdAt: datetime.datetime
    creator: "User"
    date: datetime.datetime
    description: str
    handSyncEnabled: bool
    isDeleted: str
    isGlobal: bool
    manualOrderLabels: str
    name: str
    stats: str
    milestoneProjects: List["MilestoneProject"]
    cards: List["Card"]
    activities: List["Activity"]
    progress: List["MilestoneProgress"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ProjectOrder(_BaseModel):
    account: "Account"
    project: "Project"
    sortIndex: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ProjectSelection(_BaseModel):
    account: "Account"
    project: "Project"
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ProjectTag(_BaseModel):
    color: str
    createdAt: datetime.datetime
    emoji: str
    project: "Project"
    tag: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ProjectUserSetting(_BaseModel):
    project: "Project"
    receivePublicProjectDigest: bool
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ProjectUser(_BaseModel):
    account: "Account"
    project: "Project"
    projectRole: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Project(_BaseModel):
    account: "Account"
    accountSeq: int
    allowUpvotes: bool
    commentsArePublic: bool
    coverFile: "File"
    createdAt: datetime.datetime
    defaultUserAccess: str
    id: str
    isPublic: bool
    markerColor: Any
    name: str
    publicBackgroundColor: str
    publicBackgroundImage: "File"
    publicBannerFile: "File"
    publicHeading: str
    publicIsExplicit: bool
    publicLayoutVersion: int
    publicMessage: str
    publicPath: str
    publicRegistryAgreement: bool
    publicTileFile: "File"
    visibility: str
    decks: List["Deck"]
    deckPublicOrders: List["DeckPublicOrder"]
    milestoneProjects: List["MilestoneProject"]
    publicProjectVisits: List["PublicProjectVisit"]
    dailyPublicProjectMembership: List["DailyPublicProjectMembership"]
    publicProjectMemberships: List["PublicProjectMembership"]
    cardUpvotes: List["CardUpvote"]
    cards: List["Card"]
    tags: List["ProjectTag"]
    activities: List["Activity"]
    explicitProjectUsers: List["ProjectUser"]
    access: List["UserProjectAccess"]
    publicProjectInfo: "PublicProjectInfo"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class PublicProjectInfo(_BaseModel):
    account: "Account"
    activities7d: str
    cardCount: str
    cardDoneStreak: str
    lastActivityAt: str
    project: "Project"
    visits7d: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class PublicProjectMembership(_BaseModel):
    createdAt: datetime.datetime
    digestFrequencyInDays: int
    project: "Project"
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class QueueEntry(_BaseModel):
    account: "Account"
    card: "Card"
    cardDoneAt: datetime.datetime
    createdAt: datetime.datetime
    isCleared: bool
    sortIndex: int
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class QueueSelection(_BaseModel):
    account: "Account"
    queueUser: "User"
    sortIndex: int
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Release(_BaseModel):
    content: str
    createdAt: datetime.datetime
    isLive: str
    title: str
    version: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ResolvableEntryHistory(_BaseModel):
    author: "User"
    content: str
    lastChangedAt: datetime.datetime
    resolvable: "Resolvable"
    version: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ResolvableEntry(_BaseModel):
    author: "User"
    content: str
    createdAt: datetime.datetime
    lastChangedAt: datetime.datetime
    meta: str
    resolvable: "Resolvable"
    version: str
    histories: List["ResolvableEntryHistory"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ResolvableNotification(_BaseModel):
    account: "Account"
    createdAt: datetime.datetime
    isLastParticipant: bool
    isParticipating: bool
    isSnoozing: bool
    lastUpdatedAt: datetime.datetime
    latestEntry: "ResolvableEntry"
    latestSeenEntry: "ResolvableEntry"
    resolvable: "Resolvable"
    snoozeUntil: datetime.datetime
    unseenAuthors: list
    unseenEntryCount: int
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ResolvableParticipantHistory(_BaseModel):
    addedBy: "User"
    done: bool
    firstJoinedAt: str
    lastChangedAt: datetime.datetime
    resolvable: "Resolvable"
    user: "User"
    version: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ResolvableParticipant(_BaseModel):
    account: "Account"
    addedBy: "User"
    discordUserId: str
    done: bool
    firstJoinedAt: str
    lastChangedAt: str
    resolvable: "Resolvable"
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Resolvable(_BaseModel):
    account: "Account"
    card: "Card"
    closedAt: datetime.datetime
    closedBy: "User"
    context: str
    contextAsPrio: str
    createdAt: datetime.datetime
    creator: "User"
    isClosed: str
    isPublic: bool
    participants: List["ResolvableParticipant"]
    participantHistories: List["ResolvableParticipantHistory"]
    entries: List["ResolvableEntry"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class SavedSearch(_BaseModel):
    account: "Account"
    forceOr: bool
    owner: "User"
    tokens: list

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class StripeAccountSync(_BaseModel):
    account: "Account"
    billingCycleEnd: datetime.datetime
    billingCycleStart: datetime.datetime
    centsPerSeat: int
    euVatIdData: str
    grossActualBalance: int
    grossBonusBalance: int
    hasBeenCancelledAt: datetime.datetime
    netGiftBalance: int
    paymentMethod: str
    pendingPlanType: str
    planName: str
    planType: str
    repeatingCoupon: str
    status: str
    vatCountryCode: str
    vatTaxPercentage: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class TimeTrackingSegment(_BaseModel):
    account: "Account"
    addedManually: bool
    card: "Card"
    createdAt: datetime.datetime
    finishedAt: datetime.datetime
    modifyDurationMsBy: int
    startedAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class TimeTrackingSum(_BaseModel):
    card: "Card"
    runningModifyDurationMsBy: int
    runningStartedAt: datetime.datetime
    sumMs: int
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserDismissedHint(_BaseModel):
    createdAt: datetime.datetime
    hintKey: str
    returnAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserEmail(_BaseModel):
    createdAt: datetime.datetime
    email: str
    isPrimary: str
    isVerified: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserInvitation(_BaseModel):
    accessToProjectIds: list
    account: "Account"
    createdAt: datetime.datetime
    email: str
    inviter: "User"
    role: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserInviteCode(_BaseModel):
    accessToProjectIds: list
    account: "Account"
    createdAt: datetime.datetime
    creator: "User"
    isActive: bool
    role: str
    token: str
    useCount: int
    validUntil: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserOnboarding(_BaseModel):
    steps: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserProjectAccess(_BaseModel):
    project: "Project"
    projectRole: str
    role: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserTag(_BaseModel):
    account: "Account"
    createdAt: datetime.datetime
    tag: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class User(_BaseModel):
    autoMeFilterCardLimit: int
    cdxRole: str
    createdAt: datetime.datetime
    disableAnimations: bool
    disableMovingImages: bool
    disableSpellcheck: bool
    fullName: str
    hasPassword: str
    isIntegration: bool
    lastSeenRelease: "Release"
    name: str
    profileImage: "File"
    showCardIdInTimer: bool
    statusColorPalette: str
    timezone: str
    wantsConvoDigestMail: bool
    wantsDailyDigestMail: bool
    wantsNewsletter: bool
    deckOrders: List["DeckOrder"]
    projectOrders: List["ProjectOrder"]
    projectSelections: List["ProjectSelection"]
    queueSelections: List["QueueSelection"]
    accountRoles: List["AccountRole"]
    cardDiffNotifications: List["CardDiffNotification"]
    resolvableNotifications: List["ResolvableNotification"]
    publicProjectMembership: List["PublicProjectMembership"]
    lastSeenCardUpvotes: List["LastSeenCardUpvote"]
    dueCards: List["DueCard"]
    savedSearches: List["SavedSearch"]
    activities: List["Activity"]
    emails: List["UserEmail"]
    tags: List["UserTag"]
    unverifiedEmails: List["UserEmail"]
    primaryEmail: "UserEmail"
    pinnedMilestone: "Milestone"
    explicitProjectAccess: List["ProjectUser"]
    withProjectAccess: List["UserProjectAccess"]
    projectSettings: List["ProjectUserSetting"]
    accountSettings: List["AccountUserSetting"]
    dismissedHints: List["UserDismissedHint"]
    slackIntegrations: List["Integration"]
    activeTimeTracker: "ActiveTimeTracker"
    participations: List["ResolvableParticipant"]
    upvotes: List["CardUpvote"]
    userOnboarding: "UserOnboarding"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserReportEmail(_BaseModel):
    account: "Account"
    createdAt: datetime.datetime
    email: str
    enabled: str
    userReportSetting: "UserReportSetting"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserReportSetting(_BaseModel):
    account: "Account"
    createdAt: datetime.datetime
    deckMapping: str
    fileSizeBytesLimit: int
    id: str
    name: str
    prioMapping: str
    reportTokens: List["UserReportToken"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserReportToken(_BaseModel):
    createdAt: datetime.datetime
    enabled: str
    label: str
    reportCount: int
    userReportSetting: "UserReportSetting"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Wizard(_BaseModel):
    account: "Account"
    createdAt: datetime.datetime
    currentStep: str
    data: str
    finishedAt: datetime.datetime
    name: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class WorkflowItemHistory(_BaseModel):
    account: "Account"
    changer: "User"
    diff: str
    version: int
    versionCreatedAt: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class WorkflowItem(_BaseModel):
    account: "Account"
    accountSeq: str
    assignee: "User"
    checkboxInfo: list
    checkboxStats: str
    content: str
    createdAt: datetime.datetime
    creator: "User"
    deck: "Deck"
    effort: Any
    lastUpdatedAt: datetime.datetime
    masterTags: list
    mentionedUsers: list
    priority: str
    sortOrder: str
    tags: list
    targetDeck: "Deck"
    title: str
    version: str
    visibility: str
    diffs: List["WorkflowItemHistory"]
    inDeps: List["WorkflowItem"]
    outDeps: List["WorkflowItem"]

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)
