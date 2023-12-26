from typing import List, Any, Optional
import datetime
from enum import Enum

from .models import _BaseModel


class FieldEnum(Enum):
    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value


class Root(_BaseModel):
    class Relations(FieldEnum):
        releases = "releases"
        accountOnboardingSteps = "accountOnboardingSteps"
        account = "account"
        loggedInUser = "loggedInUser"
        cardsStatusHistory = "cardsStatusHistory"
        cardsEffortHistory = "cardsEffortHistory"
        cardsFinishedHistory = "cardsFinishedHistory"
        cardsTimeToFinished = "cardsTimeToFinished"

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
    class Fields(FieldEnum):
        chapter = "chapter"
        description = "description"
        milestone = "milestone"
        sortValue = "sortValue"
        title = "title"
        variants = "variants"
        xp = "xp"

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
    class Fields(FieldEnum):
        account = "account"
        steps = "steps"
        variants = "variants"

    account: "Account"
    steps: str
    variants: list

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AccountRole(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        createdAt = "createdAt"
        isBillingContact = "isBillingContact"
        lastChangedAt = "lastChangedAt"
        role = "role"
        user = "user"

    account: "Account"
    createdAt: datetime.datetime
    isBillingContact: str
    lastChangedAt: datetime.datetime
    role: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AccountSetting(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        key = "key"
        usesDefault = "usesDefault"
        value = "value"

    account: "Account"
    key: str
    usesDefault: str
    value: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AccountUserAchievement(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        context = "context"
        user = "user"
        value = "value"

    account: "Account"
    context: str
    user: "User"
    value: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AccountUserSetting(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        inboxDeck = "inboxDeck"
        user = "user"

    account: "Account"
    inboxDeck: "Deck"
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Account(_BaseModel):
    class Fields(FieldEnum):
        activeFeatureFlags = "activeFeatureFlags"
        activeProjectCount = "activeProjectCount"
        allowInheritHeroCover = "allowInheritHeroCover"
        attachmentCoverMode = "attachmentCoverMode"
        billingCity = "billingCity"
        billingCountryCode = "billingCountryCode"
        billingLine1 = "billingLine1"
        billingLine2 = "billingLine2"
        billingName = "billingName"
        billingType = "billingType"
        billingZip = "billingZip"
        coupon = "coupon"
        createdAt = "createdAt"
        dependenciesEnabled = "dependenciesEnabled"
        disabledAt = "disabledAt"
        disabledBy = "disabledBy"
        effortScale = "effortScale"
        hideCompletedCardCountForDecks = "hideCompletedCardCountForDecks"
        id = "id"
        isDisabled = "isDisabled"
        isLearning = "isLearning"
        isNonProfit = "isNonProfit"
        maxHandSlotCount = "maxHandSlotCount"
        maxTimeTrackingSegmentMsDuration = "maxTimeTrackingSegmentMsDuration"
        milestonesEnabled = "milestonesEnabled"
        name = "name"
        netGiftAmount = "netGiftAmount"
        offeringTrial = "offeringTrial"
        persona = "persona"
        priorityLabels = "priorityLabels"
        seats = "seats"
        staffPermission = "staffPermission"
        statusChangeDurations = "statusChangeDurations"
        subdomain = "subdomain"
        timeTrackingMode = "timeTrackingMode"
        timeTrackingSwimLaneInfo = "timeTrackingSwimLaneInfo"
        totalMediaByteUsage = "totalMediaByteUsage"
        workdays = "workdays"
        workflowMode = "workflowMode"

    class Relations(FieldEnum):
        cards = "cards"
        invoices = "invoices"
        cardPresets = "cardPresets"
        attachments = "attachments"
        discordGuilds = "discordGuilds"
        timeTrackingSegments = "timeTrackingSegments"
        workflowItems = "workflowItems"
        deckAssignments = "deckAssignments"
        assigneeAssignments = "assigneeAssignments"
        assigneeDeckAssignments = "assigneeDeckAssignments"
        wizards = "wizards"
        milestones = "milestones"
        handCards = "handCards"
        resolvables = "resolvables"
        cardUpvotes = "cardUpvotes"
        resolvableParticipants = "resolvableParticipants"
        userReportSettings = "userReportSettings"
        cardOrders = "cardOrders"
        accountUserAchievements = "accountUserAchievements"
        userInviteCodes = "userInviteCodes"
        decks = "decks"
        queueEntries = "queueEntries"
        anyDecks = "anyDecks"
        projects = "projects"
        archivedProjects = "archivedProjects"
        anyProjects = "anyProjects"
        onboardingDeck = "onboardingDeck"
        deckSubscriptions = "deckSubscriptions"
        roles = "roles"
        invitations = "invitations"
        githubIntegration = "githubIntegration"
        slackIntegration = "slackIntegration"
        affiliateCodes = "affiliateCodes"
        activities = "activities"
        stripeAccountSync = "stripeAccountSync"
        accountOnboarding = "accountOnboarding"

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
    class Fields(FieldEnum):
        account = "account"
        card = "card"
        createdAt = "createdAt"
        user = "user"

    account: "Account"
    card: "Card"
    createdAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Activity(_BaseModel):
    class Fields(FieldEnum):
        card = "card"
        changer = "changer"
        createdAt = "createdAt"
        data = "data"
        deck = "deck"
        isRemovedFromDeckEntry = "isRemovedFromDeckEntry"
        isRemovedFromMilestoneEntry = "isRemovedFromMilestoneEntry"
        milestone = "milestone"
        project = "project"
        type = "type"

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
    class Fields(FieldEnum):
        affiliateCode = "affiliateCode"
        month = "month"
        newVisitors = "newVisitors"
        revenue = "revenue"
        signups = "signups"
        visits = "visits"
        year = "year"

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
    class Fields(FieldEnum):
        account = "account"
        code = "code"
        createdAt = "createdAt"
        creator = "creator"
        isDeleted = "isDeleted"
        isDisabled = "isDisabled"
        label = "label"
        message = "message"
        remainingRedemptions = "remainingRedemptions"
        reward = "reward"
        validUntil = "validUntil"
        vanityUrl = "vanityUrl"

    class Relations(FieldEnum):
        stats = "stats"

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
    class Fields(FieldEnum):
        account = "account"
        assignedBy = "assignedBy"
        assignee = "assignee"
        lastAssignedAt = "lastAssignedAt"

    account: "Account"
    assignedBy: "User"
    assignee: "User"
    lastAssignedAt: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class AssigneeDeckAssignment(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        assignedBy = "assignedBy"
        assignee = "assignee"
        deck = "deck"
        lastAssignedAt = "lastAssignedAt"

    account: "Account"
    assignedBy: "User"
    assignee: "User"
    deck: "Deck"
    lastAssignedAt: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Attachment(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        card = "card"
        content = "content"
        createdAt = "createdAt"
        creator = "creator"
        file = "file"
        title = "title"

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
    class Fields(FieldEnum):
        account = "account"
        asOwner = "asOwner"
        card = "card"
        changers = "changers"
        changes = "changes"
        createdAt = "createdAt"
        lastUpdatedAt = "lastUpdatedAt"
        user = "user"

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
    class Fields(FieldEnum):
        account = "account"
        card = "card"
        changer = "changer"
        diff = "diff"
        version = "version"
        versionCreatedAt = "versionCreatedAt"

    account: "Account"
    card: "Card"
    changer: "User"
    diff: str
    version: int
    versionCreatedAt: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardOrderInDeck(_BaseModel):
    class Fields(FieldEnum):
        card = "card"
        changer = "changer"
        deck = "deck"
        sortIndex = "sortIndex"

    card: "Card"
    changer: "User"
    deck: "Deck"
    sortIndex: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardOrder(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        card = "card"
        label = "label"
        sortValue = "sortValue"

    account: "Account"
    card: "Card"
    label: str
    sortValue: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardPreset(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        createdAt = "createdAt"
        creator = "creator"
        data = "data"
        name = "name"

    account: "Account"
    createdAt: datetime.datetime
    creator: "User"
    data: str
    name: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardSubscription(_BaseModel):
    class Fields(FieldEnum):
        card = "card"
        createdAt = "createdAt"
        user = "user"

    card: "Card"
    createdAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardUpvote(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        card = "card"
        createdAt = "createdAt"
        discordUserInfo = "discordUserInfo"
        type = "type"
        user = "user"

    account: "Account"
    card: "Card"
    createdAt: datetime.datetime
    discordUserInfo: str
    type: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Card(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        accountSeq = "accountSeq"
        assignee = "assignee"
        checkboxInfo = "checkboxInfo"
        checkboxStats = "checkboxStats"
        content = "content"
        coverFile = "coverFile"
        createdAt = "createdAt"
        creator = "creator"
        deck = "deck"
        discordGuild = "discordGuild"
        dueDate = "dueDate"
        effort = "effort"
        embeds = "embeds"
        hasBlockingDeps = "hasBlockingDeps"
        isDoc = "isDoc"
        isPublic = "isPublic"
        lastUpdatedAt = "lastUpdatedAt"
        legacyProject = "legacyProject"
        legacyProjectSeq = "legacyProjectSeq"
        masterTags = "masterTags"
        mentionedUsers = "mentionedUsers"
        meta = "meta"
        milestone = "milestone"
        parentCard = "parentCard"
        priority = "priority"
        sourceWorkflowItemId = "sourceWorkflowItemId"
        status = "status"
        tags = "tags"
        title = "title"
        version = "version"
        visibility = "visibility"

    class Relations(FieldEnum):
        resolvables = "resolvables"
        handCards = "handCards"
        timeTrackingSegments = "timeTrackingSegments"
        cardSubscriptions = "cardSubscriptions"
        resolvableEntries = "resolvableEntries"
        attachments = "attachments"
        diffs = "diffs"
        totalTimeTrackingSums = "totalTimeTrackingSums"
        userTimeTrackingSums = "userTimeTrackingSums"
        childCards = "childCards"
        inDeps = "inDeps"
        outDeps = "outDeps"
        cardReferences = "cardReferences"
        upvotes = "upvotes"

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
    class Fields(FieldEnum):
        cardCount = "cardCount"
        date = "date"
        effortSum = "effortSum"

    cardCount: int
    date: datetime.datetime
    effortSum: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardsFinishedHistory(_BaseModel):
    class Fields(FieldEnum):
        assignee = "assignee"
        cardCount = "cardCount"
        date = "date"
        effortSum = "effortSum"

    assignee: "User"
    cardCount: int
    date: datetime.datetime
    effortSum: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardsStatusHistory(_BaseModel):
    class Fields(FieldEnum):
        count = "count"
        date = "date"
        status = "status"

    count: int
    date: datetime.datetime
    status: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class CardsTimeToFinished(_BaseModel):
    class Fields(FieldEnum):
        assignee = "assignee"
        card = "card"
        doneAt = "doneAt"
        effort = "effort"
        startedAt = "startedAt"

    assignee: "User"
    card: "Card"
    doneAt: datetime.datetime
    effort: int
    startedAt: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DailyDiscordGuildVoteMembership(_BaseModel):
    class Fields(FieldEnum):
        discordGuild = "discordGuild"
        membershipCount = "membershipCount"
        t = "t"

    discordGuild: "DiscordGuild"
    membershipCount: int
    t: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DailyPublicProjectMembership(_BaseModel):
    class Fields(FieldEnum):
        membershipCount = "membershipCount"
        project = "project"
        t = "t"

    membershipCount: int
    project: "Project"
    t: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class PublicProjectVisit(_BaseModel):
    class Fields(FieldEnum):
        project = "project"
        t = "t"
        topReferrers = "topReferrers"
        visitCounts = "visitCounts"

    project: "Project"
    t: datetime.datetime
    topReferrers: str
    visitCounts: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DeckAssignment(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        deck = "deck"
        lastAssignedAt = "lastAssignedAt"
        user = "user"

    account: "Account"
    deck: "Deck"
    lastAssignedAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DeckOrder(_BaseModel):
    class Fields(FieldEnum):
        deck = "deck"
        project = "project"
        sortIndex = "sortIndex"
        user = "user"

    deck: "Deck"
    project: "Project"
    sortIndex: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DeckPublicOrder(_BaseModel):
    class Fields(FieldEnum):
        deck = "deck"
        project = "project"
        sortIndex = "sortIndex"

    deck: "Deck"
    project: "Project"
    sortIndex: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DeckSubscription(_BaseModel):
    class Fields(FieldEnum):
        deck = "deck"
        user = "user"

    deck: "Deck"
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Deck(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        accountSeq = "accountSeq"
        content = "content"
        coverColor = "coverColor"
        coverFile = "coverFile"
        createdAt = "createdAt"
        creator = "creator"
        defaultCard = "defaultCard"
        defaultProjectTag = "defaultProjectTag"
        handSyncEnabled = "handSyncEnabled"
        isDeleted = "isDeleted"
        isOnboardingDeck = "isOnboardingDeck"
        manualOrderLabels = "manualOrderLabels"
        milestone = "milestone"
        preferredOrder = "preferredOrder"
        project = "project"
        stats = "stats"
        stickyDefaultProjectTag = "stickyDefaultProjectTag"
        title = "title"

    class Relations(FieldEnum):
        cards = "cards"
        workflowItems = "workflowItems"
        cardOrderInDecks = "cardOrderInDecks"
        activities = "activities"

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
    class Fields(FieldEnum):
        account = "account"
        createdAt = "createdAt"
        discordGuildId = "discordGuildId"
        guildIconId = "guildIconId"
        guildName = "guildName"
        karmaRoleThresholds = "karmaRoleThresholds"
        removeCommandEmoji = "removeCommandEmoji"
        removeCommandEnabled = "removeCommandEnabled"
        removeCommandRoleId = "removeCommandRoleId"
        scope = "scope"

    class Relations(FieldEnum):
        slashCommands = "slashCommands"
        projectNotifications = "projectNotifications"
        dailyDiscordGuildVoteMemberships = "dailyDiscordGuildVoteMemberships"
        members = "members"

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
    class Fields(FieldEnum):
        avatar = "avatar"
        createdAt = "createdAt"
        deckyScore = "deckyScore"
        discordGuild = "discordGuild"
        discordUserId = "discordUserId"
        discriminator = "discriminator"
        name = "name"
        nick = "nick"

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
    class Fields(FieldEnum):
        createdAt = "createdAt"
        disabledTypes = "disabledTypes"
        discordChannelId = "discordChannelId"
        discordGuild = "discordGuild"
        project = "project"

    createdAt: datetime.datetime
    disabledTypes: str
    discordChannelId: str
    discordGuild: "DiscordGuild"
    project: "Project"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class DiscordSlashCommand(_BaseModel):
    class Fields(FieldEnum):
        autoAddRoleToThread = "autoAddRoleToThread"
        channelId = "channelId"
        deck = "deck"
        description = "description"
        discordGuild = "discordGuild"
        karmaForCompletion = "karmaForCompletion"
        leaderboard = "leaderboard"
        name = "name"
        permissions = "permissions"
        reaction = "reaction"
        reactionThreshold = "reactionThreshold"
        statusMessages = "statusMessages"
        statusTargetChannelId = "statusTargetChannelId"

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
    class Fields(FieldEnum):
        account = "account"
        card = "card"
        createdAt = "createdAt"
        user = "user"

    account: "Account"
    card: "Card"
    createdAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class File(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        createdAt = "createdAt"
        deletedAt = "deletedAt"
        deletedBy = "deletedBy"
        isDeleted = "isDeleted"
        meta = "meta"
        name = "name"
        selfHosted = "selfHosted"
        size = "size"
        uploader = "uploader"
        url = "url"

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
    class Fields(FieldEnum):
        account = "account"
        card = "card"
        sortIndex = "sortIndex"
        user = "user"

    account: "Account"
    card: "Card"
    sortIndex: int
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Integration(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        createdAt = "createdAt"
        creator = "creator"
        disabled = "disabled"
        type = "type"
        user = "user"
        userData = "userData"
        version = "version"

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
    class Fields(FieldEnum):
        account = "account"
        chargeData = "chargeData"
        charged = "charged"
        createdAt = "createdAt"
        invoiceNumber = "invoiceNumber"
        subtotal = "subtotal"
        total = "total"
        url = "url"

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
    class Fields(FieldEnum):
        account = "account"
        createdAt = "createdAt"
        lastSeenAt = "lastSeenAt"
        user = "user"

    account: "Account"
    createdAt: datetime.datetime
    lastSeenAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class MilestoneProgress(_BaseModel):
    class Fields(FieldEnum):
        milestone = "milestone"
        progress = "progress"

    milestone: "Milestone"
    progress: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class MilestoneProject(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        milestone = "milestone"
        project = "project"

    account: "Account"
    milestone: "Milestone"
    project: "Project"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Milestone(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        accountSeq = "accountSeq"
        color = "color"
        createdAt = "createdAt"
        creator = "creator"
        date = "date"
        description = "description"
        handSyncEnabled = "handSyncEnabled"
        isDeleted = "isDeleted"
        isGlobal = "isGlobal"
        manualOrderLabels = "manualOrderLabels"
        name = "name"
        stats = "stats"

    class Relations(FieldEnum):
        milestoneProjects = "milestoneProjects"
        cards = "cards"
        activities = "activities"
        progress = "progress"

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
    class Fields(FieldEnum):
        account = "account"
        project = "project"
        sortIndex = "sortIndex"
        user = "user"

    account: "Account"
    project: "Project"
    sortIndex: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ProjectSelection(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        project = "project"
        user = "user"

    account: "Account"
    project: "Project"
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ProjectTag(_BaseModel):
    class Fields(FieldEnum):
        color = "color"
        createdAt = "createdAt"
        emoji = "emoji"
        project = "project"
        tag = "tag"

    color: str
    createdAt: datetime.datetime
    emoji: str
    project: "Project"
    tag: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ProjectUserSetting(_BaseModel):
    class Fields(FieldEnum):
        project = "project"
        receivePublicProjectDigest = "receivePublicProjectDigest"
        user = "user"

    project: "Project"
    receivePublicProjectDigest: bool
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ProjectUser(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        project = "project"
        projectRole = "projectRole"
        user = "user"

    account: "Account"
    project: "Project"
    projectRole: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Project(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        accountSeq = "accountSeq"
        allowUpvotes = "allowUpvotes"
        commentsArePublic = "commentsArePublic"
        coverFile = "coverFile"
        createdAt = "createdAt"
        defaultUserAccess = "defaultUserAccess"
        id = "id"
        isPublic = "isPublic"
        markerColor = "markerColor"
        name = "name"
        publicBackgroundColor = "publicBackgroundColor"
        publicBackgroundImage = "publicBackgroundImage"
        publicBannerFile = "publicBannerFile"
        publicHeading = "publicHeading"
        publicIsExplicit = "publicIsExplicit"
        publicLayoutVersion = "publicLayoutVersion"
        publicMessage = "publicMessage"
        publicPath = "publicPath"
        publicRegistryAgreement = "publicRegistryAgreement"
        publicTileFile = "publicTileFile"
        visibility = "visibility"

    class Relations(FieldEnum):
        decks = "decks"
        deckPublicOrders = "deckPublicOrders"
        milestoneProjects = "milestoneProjects"
        publicProjectVisits = "publicProjectVisits"
        dailyPublicProjectMembership = "dailyPublicProjectMembership"
        publicProjectMemberships = "publicProjectMemberships"
        cardUpvotes = "cardUpvotes"
        cards = "cards"
        tags = "tags"
        activities = "activities"
        explicitProjectUsers = "explicitProjectUsers"
        access = "access"
        publicProjectInfo = "publicProjectInfo"

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
    class Fields(FieldEnum):
        account = "account"
        activities7d = "activities7d"
        cardCount = "cardCount"
        cardDoneStreak = "cardDoneStreak"
        lastActivityAt = "lastActivityAt"
        project = "project"
        visits7d = "visits7d"

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
    class Fields(FieldEnum):
        createdAt = "createdAt"
        digestFrequencyInDays = "digestFrequencyInDays"
        project = "project"
        user = "user"

    createdAt: datetime.datetime
    digestFrequencyInDays: int
    project: "Project"
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class QueueEntry(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        card = "card"
        cardDoneAt = "cardDoneAt"
        createdAt = "createdAt"
        isCleared = "isCleared"
        sortIndex = "sortIndex"
        user = "user"

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
    class Fields(FieldEnum):
        account = "account"
        queueUser = "queueUser"
        sortIndex = "sortIndex"
        user = "user"

    account: "Account"
    queueUser: "User"
    sortIndex: int
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Release(_BaseModel):
    class Fields(FieldEnum):
        content = "content"
        createdAt = "createdAt"
        isLive = "isLive"
        title = "title"
        version = "version"

    content: str
    createdAt: datetime.datetime
    isLive: str
    title: str
    version: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ResolvableEntryHistory(_BaseModel):
    class Fields(FieldEnum):
        author = "author"
        content = "content"
        lastChangedAt = "lastChangedAt"
        resolvable = "resolvable"
        version = "version"

    author: "User"
    content: str
    lastChangedAt: datetime.datetime
    resolvable: "Resolvable"
    version: int

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class ResolvableEntry(_BaseModel):
    class Fields(FieldEnum):
        author = "author"
        content = "content"
        createdAt = "createdAt"
        lastChangedAt = "lastChangedAt"
        meta = "meta"
        resolvable = "resolvable"
        version = "version"

    class Relations(FieldEnum):
        histories = "histories"

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
    class Fields(FieldEnum):
        account = "account"
        createdAt = "createdAt"
        isLastParticipant = "isLastParticipant"
        isParticipating = "isParticipating"
        isSnoozing = "isSnoozing"
        lastUpdatedAt = "lastUpdatedAt"
        latestEntry = "latestEntry"
        latestSeenEntry = "latestSeenEntry"
        resolvable = "resolvable"
        snoozeUntil = "snoozeUntil"
        unseenAuthors = "unseenAuthors"
        unseenEntryCount = "unseenEntryCount"
        user = "user"

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
    class Fields(FieldEnum):
        addedBy = "addedBy"
        done = "done"
        firstJoinedAt = "firstJoinedAt"
        lastChangedAt = "lastChangedAt"
        resolvable = "resolvable"
        user = "user"
        version = "version"

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
    class Fields(FieldEnum):
        account = "account"
        addedBy = "addedBy"
        discordUserId = "discordUserId"
        done = "done"
        firstJoinedAt = "firstJoinedAt"
        lastChangedAt = "lastChangedAt"
        resolvable = "resolvable"
        user = "user"

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
    class Fields(FieldEnum):
        account = "account"
        card = "card"
        closedAt = "closedAt"
        closedBy = "closedBy"
        context = "context"
        contextAsPrio = "contextAsPrio"
        createdAt = "createdAt"
        creator = "creator"
        isClosed = "isClosed"
        isPublic = "isPublic"

    class Relations(FieldEnum):
        participants = "participants"
        participantHistories = "participantHistories"
        entries = "entries"

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
    class Fields(FieldEnum):
        account = "account"
        forceOr = "forceOr"
        owner = "owner"
        tokens = "tokens"

    account: "Account"
    forceOr: bool
    owner: "User"
    tokens: list

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class StripeAccountSync(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        billingCycleEnd = "billingCycleEnd"
        billingCycleStart = "billingCycleStart"
        centsPerSeat = "centsPerSeat"
        euVatIdData = "euVatIdData"
        grossActualBalance = "grossActualBalance"
        grossBonusBalance = "grossBonusBalance"
        hasBeenCancelledAt = "hasBeenCancelledAt"
        netGiftBalance = "netGiftBalance"
        paymentMethod = "paymentMethod"
        pendingPlanType = "pendingPlanType"
        planName = "planName"
        planType = "planType"
        repeatingCoupon = "repeatingCoupon"
        status = "status"
        vatCountryCode = "vatCountryCode"
        vatTaxPercentage = "vatTaxPercentage"

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
    class Fields(FieldEnum):
        account = "account"
        addedManually = "addedManually"
        card = "card"
        createdAt = "createdAt"
        finishedAt = "finishedAt"
        modifyDurationMsBy = "modifyDurationMsBy"
        startedAt = "startedAt"
        user = "user"

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
    class Fields(FieldEnum):
        card = "card"
        runningModifyDurationMsBy = "runningModifyDurationMsBy"
        runningStartedAt = "runningStartedAt"
        sumMs = "sumMs"
        user = "user"

    card: "Card"
    runningModifyDurationMsBy: int
    runningStartedAt: datetime.datetime
    sumMs: int
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserDismissedHint(_BaseModel):
    class Fields(FieldEnum):
        createdAt = "createdAt"
        hintKey = "hintKey"
        returnAt = "returnAt"
        user = "user"

    createdAt: datetime.datetime
    hintKey: str
    returnAt: datetime.datetime
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserEmail(_BaseModel):
    class Fields(FieldEnum):
        createdAt = "createdAt"
        email = "email"
        isPrimary = "isPrimary"
        isVerified = "isVerified"
        user = "user"

    createdAt: datetime.datetime
    email: str
    isPrimary: str
    isVerified: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserInvitation(_BaseModel):
    class Fields(FieldEnum):
        accessToProjectIds = "accessToProjectIds"
        account = "account"
        createdAt = "createdAt"
        email = "email"
        inviter = "inviter"
        role = "role"

    accessToProjectIds: list
    account: "Account"
    createdAt: datetime.datetime
    email: str
    inviter: "User"
    role: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserInviteCode(_BaseModel):
    class Fields(FieldEnum):
        accessToProjectIds = "accessToProjectIds"
        account = "account"
        createdAt = "createdAt"
        creator = "creator"
        isActive = "isActive"
        role = "role"
        token = "token"
        useCount = "useCount"
        validUntil = "validUntil"

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
    class Fields(FieldEnum):
        steps = "steps"
        user = "user"

    steps: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserProjectAccess(_BaseModel):
    class Fields(FieldEnum):
        project = "project"
        projectRole = "projectRole"
        role = "role"
        user = "user"

    project: "Project"
    projectRole: str
    role: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserTag(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        createdAt = "createdAt"
        tag = "tag"
        user = "user"

    account: "Account"
    createdAt: datetime.datetime
    tag: str
    user: "User"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class User(_BaseModel):
    class Fields(FieldEnum):
        autoMeFilterCardLimit = "autoMeFilterCardLimit"
        cdxRole = "cdxRole"
        createdAt = "createdAt"
        disableAnimations = "disableAnimations"
        disableMovingImages = "disableMovingImages"
        disableSpellcheck = "disableSpellcheck"
        fullName = "fullName"
        hasPassword = "hasPassword"
        isIntegration = "isIntegration"
        lastSeenRelease = "lastSeenRelease"
        name = "name"
        profileImage = "profileImage"
        showCardIdInTimer = "showCardIdInTimer"
        statusColorPalette = "statusColorPalette"
        timezone = "timezone"
        wantsConvoDigestMail = "wantsConvoDigestMail"
        wantsDailyDigestMail = "wantsDailyDigestMail"
        wantsNewsletter = "wantsNewsletter"

    class Relations(FieldEnum):
        deckOrders = "deckOrders"
        projectOrders = "projectOrders"
        projectSelections = "projectSelections"
        queueSelections = "queueSelections"
        accountRoles = "accountRoles"
        cardDiffNotifications = "cardDiffNotifications"
        resolvableNotifications = "resolvableNotifications"
        publicProjectMembership = "publicProjectMembership"
        lastSeenCardUpvotes = "lastSeenCardUpvotes"
        dueCards = "dueCards"
        savedSearches = "savedSearches"
        activities = "activities"
        emails = "emails"
        tags = "tags"
        unverifiedEmails = "unverifiedEmails"
        primaryEmail = "primaryEmail"
        pinnedMilestone = "pinnedMilestone"
        explicitProjectAccess = "explicitProjectAccess"
        withProjectAccess = "withProjectAccess"
        projectSettings = "projectSettings"
        accountSettings = "accountSettings"
        dismissedHints = "dismissedHints"
        slackIntegrations = "slackIntegrations"
        activeTimeTracker = "activeTimeTracker"
        participations = "participations"
        upvotes = "upvotes"
        userOnboarding = "userOnboarding"

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
    class Fields(FieldEnum):
        account = "account"
        createdAt = "createdAt"
        email = "email"
        enabled = "enabled"
        userReportSetting = "userReportSetting"

    account: "Account"
    createdAt: datetime.datetime
    email: str
    enabled: str
    userReportSetting: "UserReportSetting"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class UserReportSetting(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        createdAt = "createdAt"
        deckMapping = "deckMapping"
        fileSizeBytesLimit = "fileSizeBytesLimit"
        id = "id"
        name = "name"
        prioMapping = "prioMapping"

    class Relations(FieldEnum):
        reportTokens = "reportTokens"

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
    class Fields(FieldEnum):
        createdAt = "createdAt"
        enabled = "enabled"
        label = "label"
        reportCount = "reportCount"
        userReportSetting = "userReportSetting"

    createdAt: datetime.datetime
    enabled: str
    label: str
    reportCount: int
    userReportSetting: "UserReportSetting"

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class Wizard(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        createdAt = "createdAt"
        currentStep = "currentStep"
        data = "data"
        finishedAt = "finishedAt"
        name = "name"

    account: "Account"
    createdAt: datetime.datetime
    currentStep: str
    data: str
    finishedAt: datetime.datetime
    name: str

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class WorkflowItemHistory(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        changer = "changer"
        diff = "diff"
        version = "version"
        versionCreatedAt = "versionCreatedAt"

    account: "Account"
    changer: "User"
    diff: str
    version: int
    versionCreatedAt: datetime.datetime

    def __init__(self, id: str, data: Optional[dict]):
        super().__init__(id, data)


class WorkflowItem(_BaseModel):
    class Fields(FieldEnum):
        account = "account"
        accountSeq = "accountSeq"
        assignee = "assignee"
        checkboxInfo = "checkboxInfo"
        checkboxStats = "checkboxStats"
        content = "content"
        createdAt = "createdAt"
        creator = "creator"
        deck = "deck"
        effort = "effort"
        lastUpdatedAt = "lastUpdatedAt"
        masterTags = "masterTags"
        mentionedUsers = "mentionedUsers"
        priority = "priority"
        sortOrder = "sortOrder"
        tags = "tags"
        targetDeck = "targetDeck"
        title = "title"
        version = "version"
        visibility = "visibility"

    class Relations(FieldEnum):
        diffs = "diffs"
        inDeps = "inDeps"
        outDeps = "outDeps"

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
